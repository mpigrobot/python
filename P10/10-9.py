# def log(f):
#     def fn(x):
#         print 'call ' + f.__name__ + '()...'
#         return f(x)
#     return fn
def log(f):
    def fn(*args, **kw):
        print 'call ' + f.__name__ + '()...'
        return f(*args, **kw)
    return fn
@log
def add(x, y):
    return x + y
print add(1, 2)