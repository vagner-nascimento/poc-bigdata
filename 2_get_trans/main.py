import sys
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

if __name__ == "__main__":
    arg = sys.argv[1]
    year = int(arg)

    print("getting transactions for the year " + arg)
    trans = get_transactions(year)
    print("transactions goten: " + str(len(trans)))

    print("copying transactions for big data database")
    save_transactions(trans)
    print("transactions copied for big data database")
