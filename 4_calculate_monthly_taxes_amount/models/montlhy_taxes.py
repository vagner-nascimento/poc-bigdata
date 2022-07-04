from models.monthly_amount import MonthlyAmount

class MonthlyTaxes:
    def __init__(self, month_amount: MonthlyAmount, taxes: int) -> None:
        self._id = month_amount._id
        self.amount = month_amount.amount
        self.taxes = taxes
