import sys

from functions.data.monthly_amount import get_monthly_amount
from functions.data.monthly_taxes import get_monthly_taxes, save_monthly_taxes

if __name__ == "__main__":
    arg_year = sys.argv[1]
    arg_month = sys.argv[2]
    year = int(arg_year)
    month = int(arg_month)

    print("getting monthly amount for {}/{}".format(year, month))
    mont_amount = get_monthly_amount(year, month)

    print("getting monthly taxes for {}/{}".format(year, month))
    month_taxes = get_monthly_taxes(mont_amount)

    print("saving monthly taxes for {}/{}".format(year, month))
    save_monthly_taxes(month_taxes)
    print("monthly taxes saved for {}/{}".format(year, month))
