class Rational(object):
    def __init__(self, p, q):
        self.p = p
        self.q = q
    def __int__(self):
        return self.p // self.q
print int(Rational(7, 2))
print int(Rational(1, 3))