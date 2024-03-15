class Radius(object):
    
    radius = 0
    pi = 3.14

    def __init__(self, radius):
        self.radius = radius

    def diameter(self):
        return float(2 * self.radius)
    
    def circumference(self):
        d = self.diameter()
        return d * self.pi
    
    def area(self):
        return self.pi * (self.radius * self.radius)

    def volume(self):
        return 4/3 * self.pi * pow(self.radius, 3)

r = Radius(5)
print(r.diameter())
print(r.circumference())
print(r.area())
print(r.volume())