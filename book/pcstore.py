class PcStore:

    """
    o enunciado deste exercício (5) é péssimo
    """

    start_pay_rate = 0.10
    annual_rate = 0.12
    monthly_payment_rate = 0.5

    def __init__(self, price):
        self.price = price
        self.set_balance(price * (self.start_pay_rate - 1))

    def monthly_payment(self):
        return self.monthly_payment_rate * self.start_payment()
    
    def total_months(self):
        return self.get_balance() / self.monthly_payment()

    def start_payment(self):
        return self.price * self.start_pay_rate
    
    def month_interest(self):
        return self.balance * (self.annual_rate / 12)
    
    def principal_month_value(self):
        return self.monthly_payment() - self.month_interest()
    
    def set_balance(self, paid):
        if self.balance == 0: self.balance = self.price - self.start_payment()
        else: self.balance -= paid

    def get_balance(self):
        return self.balance
    
pc = PcStore(1000)
print(pc.total_months())
    