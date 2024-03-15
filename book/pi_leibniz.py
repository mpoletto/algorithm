class PiLeibniz:
    
    pi = 3.1416

    def __init__(self, times):
        self.times = times

    def aproximate(self):
        # Leibniz method to aproximate PI number: PI/4 = 1 - 1/3 + 1/5 - 1/7 ...
        soma = 0
        for i in range(self.times):
            termo = (-1) ** i / (2 * i + 1) 
            soma += termo
        return soma * 4

if __name__ == "__main__":
    pl = PiLeibniz(int(input()))
    print(pl.aproximate())            

