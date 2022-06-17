import sys

def get_transactions_monthly_amount(year, month):
    query = { "_id": { "year": year, "month": month } }

    from db import get_bigdata_db
    bd_db = get_bigdata_db()
    mont_amount = bd_db.trans_monthly_amount.find_one(query)

    return mont_amount

def get_total_taxes(mont_amount):
    year = mont_amount["_id"]["year"]
    month = mont_amount["_id"]["month"]
    total_amount = mont_amount["totalAmount"]
    
    from taxes_client import get_month_total_taxes
    res = get_month_total_taxes(year, month, total_amount)
    
    return { "_id": { "year": year, "month": month}, "totalAmount": total_amount, "totalTaxes": res["totalTaxes"] }

def save_total_taxes(total):
    from db import get_bigdata_db
    bd_db = get_bigdata_db()
    bd_db.trans_monthly_taxes_amount.insert_one(total)

if __name__ == "__main__":
    arg_year = sys.argv[1]
    arg_month = sys.argv[2]
    year = int(arg_year)
    month = int(arg_month)
    msg_end = "for " + arg_year + "/" + arg_month

    print("getting monthly amount " + msg_end)
    mont_amount = get_transactions_monthly_amount(year, month)

    print("getting total taxes amount " + msg_end)
    total_taxes = get_total_taxes(mont_amount)

    print("saving total taxes " + msg_end)
    save_total_taxes(total_taxes)
    print("total taxes saved " + msg_end)
