def new_fn(f):
    def fn(x):
        print 'call ' + f.__name__ + '()...'
        return f(x)
    return fn
def f1(x):
    return x*x
# g1 = new_fn(f1)
# print g1(5)
f1 = new_fn(f1)
print f1(5)
