import sys, calendar, os
from datetime import datetime

def get_transactions_total_amount(year, month):
    last_day = calendar.monthrange(year, month)[1]
    start = datetime(year, month, 1, 0, 0, 0, 0)
    end = datetime(year, month, last_day, 23, 59, 59, 999)
    query = {"$and":[{"datetime_transaction":{"$gte":start}},{"datetime_transaction":{"$lte":end}}]}

    from db import get_bigdata_db
    bd_db = get_bigdata_db()
    cur = bd_db.transactions.find(query)

    total_amount = 0
    for it in cur:
        total_amount = total_amount + it["amount"]
    
    return { "_id": { "year": year, "month": month }, "totalAmount": total_amount }

def save_total_amount(total):
    from db import get_bigdata_db
    bd_db = get_bigdata_db()
    bd_db.trans_monthly_amount.insert_one(total)

if __name__ == "__main__":
    arg_year = sys.argv[1]
    arg_month = sys.argv[2]
    year = int(arg_year)
    month = int(arg_month)
    msg_end = "for " + arg_year + "/" + arg_month

    print("getting total amount " + msg_end)
    total_amount = get_transactions_total_amount(year, month)

    print("saving total amount " + msg_end)
    save_total_amount(total_amount)
    print("total amount saved " + msg_end)

    # call next step: calculate taxes over total amount
    cmd = "python 4_calculate_monthly_taxes_amount\\main.py " + arg_year + " " + arg_month
    os.system(cmd)
