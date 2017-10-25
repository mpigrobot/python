def log_decorator(f):
    def wrapper(*args, **kw):
        print '[%s] %s()...' % (prefix, f.__name__)
        return f(*args, **kw)
    return wrapper
return log_decorator
def log(prefix):
    return log_decorator(f)