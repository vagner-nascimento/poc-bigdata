import urllib.request, json

from models.montlhy_taxes import MonthlyTaxes
from models.monthly_amount import MonthlyAmount

from libs.db import get_bigdata_db

db_db = get_bigdata_db()

COLLECTION_NAME = "trans_monthly_taxes"

# This HTTP call should be into a custom rest lib
def get_monthly_taxes(month_amount: MonthlyAmount) -> MonthlyTaxes:
    # build call url
    year = month_amount._id["year"]
    month = month_amount._id["month"]
    amount = month_amount.amount
    url = "http://localhost/tax?year={}&month={}&amount={}".format(year, month, amount)

    # do request
    res_bys = urllib.request.urlopen(url).read()

    # parse respose
    res_str = res_bys.decode("utf8").replace("'", '"')
    data = json.loads(res_str)
    res = MonthlyTaxes(month_amount, data["totalTaxes"])

    return res

def save_monthly_taxes(month_taxes: MonthlyTaxes) -> None:
    db_db[COLLECTION_NAME].insert_one(month_taxes.__dict__)
