#!/usr/bin/python
# -*- coding: utf-8 -*-
# 希望一次返回3个函数，分别计算1x1,2x2,3x3:
def count():
    fs = []
    for i in range(1, 4):
        def f(j=i):
            def g():
                return j*j
            return g
        r = f(i)
        fs.append(r)
    return fs
f1, f2, f3 = count()
print f1(), f2(), f3()