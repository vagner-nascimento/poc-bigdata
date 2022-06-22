import asyncio

from db import get_tranctions_db, get_bigdata_db

trans_db = get_tranctions_db()
bd_db = get_bigdata_db()

def get_distinct_seller_ids():
    return trans_db.transactions.distinct("seller_id")

def get_paginated_transactions(seller_id: str):
    # use projection to select only desired fields
    """
    projection:
    {
        "payment_id": 1,
        "seller_id": 1,
        "amount": 1,
        "operation": 1,
        "transaction_channel_type": 1,
        "currency": 1,
        "datetime_transaction": 1,
        "country": 1,
        "status": 1,
        
        "card.brand": 1
    }
    """
    trans = trans_db.transactions.find({ "seller_id": seller_id })
#    .sort("datetime_transaction", pymongo.ASCENDING)
    # the "sort" throws error of Mongo Server memory not egnoth to sort running local on docker

    MAX_ITENS = 100
    res = []
    cur_trans = []
    page = 1
    day = 0
    year = 0
    month = 0
    first = True
    for t in trans:
        cur_date = t["datetime_transaction"]
        cur_day = cur_date.day
        cur_month = cur_date.month
        cur_year = cur_date.year
        not_first_has_trans = not first and len(cur_trans) > 0

        if cur_year > year:
            if not_first_has_trans:
                res.append(get_trans_page(seller_id, year, month, day, page, cur_trans))
                cur_trans = []
                page = 1

            month = 1
            day = 1
            year = cur_year

        if cur_month > month:
            if not_first_has_trans:
                res.append(get_trans_page(seller_id, year, month, day, page, cur_trans))
                cur_trans = []
                page = 1

            day = 1
            month = cur_month

        if cur_day > day:
            if not_first_has_trans:
                res.append(get_trans_page(seller_id, year, month, day, page, cur_trans))
                cur_trans = []
                page = 1

            day = cur_day

        if len(cur_trans) == MAX_ITENS:
            res.append(get_trans_page(seller_id, year, month, day, page, cur_trans))
            cur_trans = []
            page = page + 1

        if page == 2:
            print("seller page > 1: " + seller_id + " - year: " + str(year) + " month: " + str(month) + " day: " + str(day) + " page: " + str(page))

        first = False
        cur_trans.append(t)

    # inserts remnants transactions
    if len(cur_trans) > 0:
        res.append(get_trans_page(seller_id, year, month, day, page, cur_trans))

    return res

def get_trans_page(seller_id: str, year: int, month: int, day: int, page: int, trans: list):
    return { "_id": { "seller_id": seller_id, "year": year, "month": month, "day": day, "page": page }, "transactions": trans }

def save_seller_transactions(seller_id: str):
#    print("getting paginated transactions for seller " + seller_id)
    pag_trans = get_paginated_transactions(seller_id)
    bd_db.trans_by_seller_paginated.insert_many(pag_trans)
#    print("paginated transactions saved for seller " + seller_id)

async def process_async(sellers_ids):
    threads = []
    for i in range(1, len(sellers_ids)): # skip first (elem 0) because is empty string
        threads.append(asyncio.to_thread(save_seller_transactions, seller_id = sellers_ids[i]))

    await asyncio.gather(*threads)

if __name__ == "__main__":
    ids = get_distinct_seller_ids()
    asyncio.run(process_async(ids))
    print("all data were processed!!")
