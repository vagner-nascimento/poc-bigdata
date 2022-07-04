from models.monthly_amount import MonthlyAmount
from libs.db import get_bigdata_db

bd_db = get_bigdata_db()

COLLECTION_NAME = "trans_monthly_amount"

def save_monthly_amount(year: int, month: int, amount: int) -> MonthlyAmount:
    month_amount = MonthlyAmount(year, month, amount)
    bd_db[COLLECTION_NAME].insert_one(month_amount.__dict__)

    return month_amount
