def log(f):
    def wrapper(*args, **kw):
        print 'call...'
        return f(*args, **kw)
    wrapper.__name__ = f.__name__
    wrapper.__doc__ = f.__doc__
    return wrapper
@log
def f2(x):
    pass
print f2.__name__