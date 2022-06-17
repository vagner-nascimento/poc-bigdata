import sys, os, asyncio
from datetime import datetime

def get_transactions(year):
    start = datetime(year, 1, 1, 0, 0, 0, 0)
    end = datetime(year, 12, 31, 23, 59, 59, 999)
    query = {"$and":[{"datetime_transaction":{"$gte":start}},{"datetime_transaction":{"$lte":end}}]}
    project = { "payment_id": 1, "amount": 1, "datetime_transaction": 1}

    from db import get_tranctions_db
    trans_db = get_tranctions_db()
    cursor = trans_db.transactions.find(query, project)
    
    trans = []
    for res in cursor:
        trans.append(res)
    
    return trans

def save_transactions(trans = []):
    from db import get_bigdata_db
    bd_db = get_bigdata_db()
    bd_db.transactions.insert_many(trans)

def calculate_monthly_amount(year, month):
    cmd = "python 3_calculate_monthly_amount\\main.py " + year + " " + month
    os.system(cmd)

# calculates total amount of all months year asynchronous
async def calculate_monthly_amounts(year):
    threads = []
    for month in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]:
        threads.append(asyncio.to_thread(calculate_monthly_amount, year = year, month = month))
    
    asyncio.gather(*threads)

if __name__ == "__main__":
    arg_year = sys.argv[1]
    year = int(arg_year)

    print("getting transactions for the year " + arg_year)
    trans = get_transactions(year)
    print("transactions goten: " + str(len(trans)))

    print("copying transactions for big data database")
    save_transactions(trans)
    print("transactions copied for big data database")

    # call next steps async: calculate total amount
    asyncio.run(calculate_monthly_amounts(arg_year))
