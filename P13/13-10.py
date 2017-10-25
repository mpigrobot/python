class Rational(object):
    def __init__(self, p, q):
        self.p = p
        self.q = q

    def __float__(self):
        return float(self.p) / self.q

print float(Rational(7, 2))
print float(Rational(6, 3))
print float(Rational(1, 3))