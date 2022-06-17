import sys, os
from datetime import datetime
from db import get_bigdata_db

bd_db = get_bigdata_db()

def delete_transactions_and_reports(year):
    # delete transactions
    start = datetime(year, 1, 1, 0, 0, 0, 0)
    end = datetime(year, 12, 31, 23, 59, 59, 999)
    query = {"$and":[{"datetime_transaction":{"$gte":start}},{"datetime_transaction":{"$lte":end}}]}
    bd_db.transactions.delete_many(query)

    # delete monthly amount report
    query = { "_id.year": year }
    bd_db.trans_monthly_amount.delete_many(query)
    bd_db.trans_monthly_taxes_amount.delete_many(query)

if __name__ == "__main__":
    arg_year = sys.argv[1]
    year = int(arg_year)
    ini_msg = "transactions and reports for the year " + arg_year
    print(ini_msg + " will be deleted")

    delete_transactions_and_reports(year)
    print(ini_msg + " were deleted")

    # call next step: get transactions
    cmd = "python 2_get_trans\\main.py " + arg_year
    os.system(cmd)
