def f(x):
    return x*x
l = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
def is_odd(x):
    return x % 2 == 1
a = filter(is_odd, l)
def reversed_cmp(x, y):
    if x > y:
        return -1
    if x < y:
        return 1
    return 0
b = sorted(a, reversed_cmp)
def calc_prod(lst):
    def lazy_prod():
        def f(x, y):
            return x * y
        return reduce(f, lst, 1)
    return lazy_prod
f = calc_prod(b)
print f()
