from models.monthly_amount import MonthlyAmount
from libs.db import get_bigdata_db

bd_db = get_bigdata_db()

COLLECTION_NAME = "trans_monthly_amount"

def get_monthly_amount(year: int, month: int) -> MonthlyAmount:
    query = { "_id": { "year": year, "month": month } }
    data = bd_db[COLLECTION_NAME].find_one(query)

    res = MonthlyAmount(data["_id"]["year"], data["_id"]["month"], data["amount"])

    return res
