#!/usr/bin/python
# -*- coding: utf-8 -*-
class Fib(object):                   #斐波那契数列是由 0, 1, 1, 2, 3, 5, 8, 13...构成。
    def __init__(self, num):
        a, b, L = 0, 1, []
        for n in range(num):
            L.append(a)
            a, b = b, a + b
        self.numbers = L

    def __str__(self):
        return str(self.numbers)

    __repr__ = __str__

    def __len__(self):
        return len(self.numbers)

f = Fib(10)
print f
print len(f)