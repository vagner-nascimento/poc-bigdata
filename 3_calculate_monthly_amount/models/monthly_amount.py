class MonthlyAmount:
    def __init__(self, year: int, month: int, amount: int) -> None:
        self._id = { "year": year, "month": month }
        self.amount = amount
