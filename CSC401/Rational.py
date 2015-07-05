class Rational:
    
    def __init__(self, n, d):
        self.numer = n
        self.denom = d

    def getdenom(self):
        return self.denom

    def getnumer(self):
        return self.numer
    
    def get(self):
        return (self.numer, self.denom)

    def __mul__(self, other):
        prodcut = Rational(self.getnumer() * other.getnumer(), self.getdenom() * other.getdenom())
        return product

    def __add__(self, other):
    
##def multiplyRational(r1, r2):
##    rp = Rational(r1.getnumer() * r2.getnumer(), r1.getdenom() * r2.getdenom())
##    return rp
    
