from datetime import datetime

class Transaction:
    def __init__(self, payment_id: str, amount: int, datetime_transaction: datetime) -> None:
        self.payment_id = payment_id
        self.amount = amount
        self.datetime_transaction = datetime_transaction
