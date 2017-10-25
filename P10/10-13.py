import time
def performance(unit):
    def perf_decorator(f):
        def wrapper(*args, **kw):
            t1 = time.time()
            r = f(*args, **kw)
            t2 = time.time()
            try:
                if unit=='ms':
                    t = (t2 - t1) * 1000
                if unit=='s':
                    t = (t2 - t1)
                print 'call %s() in %f %s' % (f.__name__, t, unit)
            except:
                print 'unit set error'
            return r
        return wrapper
    return perf_decorator

@performance('ms')
def factorial(n):
    return reduce(lambda x,y: x*y, range(1, n+1))
print factorial(10)