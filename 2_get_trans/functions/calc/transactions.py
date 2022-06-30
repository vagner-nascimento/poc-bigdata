import asyncio, os

def calculate_monthly_amount(year: int, month: int) -> None:
    cmd = "python 3_calculate_monthly_amount\\main.py " + str(year) + " " + str(month)
    os.system(cmd)

async def calculate_monthly_amounts(year: int) -> None:
    threads = []
    for month in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]:
        threads.append(asyncio.to_thread(calculate_monthly_amount, year = year, month = month))
    
    asyncio.gather(*threads)
