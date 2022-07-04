# TODO: think how to share common models throug the Data Product scripts
class MonthlyAmount:
    def __init__(self, year: int, month: int, amount: int) -> None:
        self._id = { "year": year, "month": month }
        self.amount = amount
