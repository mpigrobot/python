#!/usr/bin/python
# -*- coding: utf-8 -*-
def log(f):
    def fn(x):
        print 'call ' + f.__name__ + '()...'
        return f(x)
    return fn
# 装饰器函数
@log
def factorial(n):
    return reduce(lambda x,y: x*y, range(1, n+1))
print factorial(10)