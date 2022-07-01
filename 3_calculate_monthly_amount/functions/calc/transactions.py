import os

from pymongo.cursor import Cursor

def calculate_monthly_amount(trans: Cursor) -> int:
    total_amount = 0
    for t in trans:
        total_amount = total_amount + t["amount"]

    return total_amount

def calculate_monthly_taxes(year: int, month: int) -> None:
    cmd = "python 4_calculate_monthly_taxes_amount\\main.py {} {}".format(year, month)
    #os.system(cmd) TODO: uncoment and refactor script 4
