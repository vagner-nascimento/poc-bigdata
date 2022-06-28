import sys, os
from functions.data.transactions import delete_transactions
from functions.data.monthly_amount import delete_monthly_amount
from functions.data.monthly_taxes import delete_monthly_taxes

if __name__ == "__main__":
    arg_year = sys.argv[1]
    year = int(arg_year)
    print("transactions will be deleted for the year " + arg_year)
    delete_transactions(year)
    print("transactions deleted for the year " + arg_year)

    # TODO: call las two async and describe a patter to use async
    print("calculated monthly amount will be deleted for the year " + arg_year)
    delete_monthly_amount(year)
    print("calculated monthly amount deleted for the year " + arg_year)

    print("calculated monthly taxes will be deleted for the year " + arg_year)
    delete_monthly_taxes(year)
    print("calculated monthly taxes deleted for the year " + arg_year)

    # call next step: get transactions
    cmd = "python 2_get_trans\\main.py " + arg_year
    #os.system(cmd)
