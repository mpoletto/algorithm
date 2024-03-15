class Bounce:

    bounce_rate = 0.6

    def __init__(self, height, times):
        self.height = height
        self.times = times

    def distance(self):
        d = self.height
        tmp = self.height * self.bounce_rate
        for t in range(self.times):
            d += tmp
            tmp = tmp * self.bounce_rate
        return d

b = Bounce(10, 3)
print(b.distance())
