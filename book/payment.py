class Payment():

    ewh_rate = 1.5

    def __init__(self, hour_salary, regular_worked_hours, exceptional_worked_hours):
        self.hs = hour_salary
        self.rwh = regular_worked_hours
        self.ewh = exceptional_worked_hours

    def regular_amount(self):
        return self.hs * self.rwh
    
    def extra_amount(self):
        return self.hs * (self.ewh * self.ewh_rate)

    def week_amount(self):
        return self.regular_amount() + self.extra_amount()
    
p = Payment(50, 8, 4)
print(p.week_amount())
