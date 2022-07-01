import sys

from functions.data.transactions import get_transactions
from functions.data.monthly_amount import save_monthly_amount
from functions.calc.transactions import calculate_monthly_amount, calculate_monthly_taxes

if __name__ == "__main__":
    arg_year = sys.argv[1]
    arg_month = sys.argv[2]
    year = int(arg_year)
    month = int(arg_month)

    print("getting transactions of {}/{}".format(year, month))
    trans = get_transactions(year, month)

    print("calculating total amount of {}/{}".format(year, month))
    total_amount = calculate_monthly_amount(trans)

    print("saving total amount of {}/{}".format(year, month))
    month_amount = save_monthly_amount(year, month, total_amount)
    print("total amount of {}/{} saved".format(year, month))
    print(month_amount.__dict__)

    print("calling next step: calculate monthly taxes for {}/{}".format(year, month))
    calculate_monthly_taxes(year, month)
