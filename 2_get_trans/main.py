import sys, asyncio
from functions.data.transactions import get_transactions, save_transactions_into_bigdata
from functions.calc.transactions import calculate_monthly_amounts

if __name__ == "__main__":
    str_year = sys.argv[1]
    year = int(str_year)

    print("getting transactions for the year " + str_year)
    trans = get_transactions(year)
    print("transactions goten: " + str(len(trans)))

    print("saving transactions into big data database")
    save_transactions_into_bigdata(trans)
    print("transactions saved into big data database")

    # call next steps async: calculate total monthly amount
    print("calling monthly amounts calculation asynchronous for each month of the year " + str_year)
    asyncio.run(calculate_monthly_amounts(year))
    print("monthly amounts calculated for each month of the year " + str_year)
