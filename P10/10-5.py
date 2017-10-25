#!/usr/bin/python
# -*- coding: utf-8 -*-
# 可以不必定义函数名，直接创建一个函数对象:
print sorted([1, 3, 9, 5, 0], lambda x, y: -cmp(x, y))
# 使用匿名函数，可以不必定义函数名，直接创建一个函数对象，很多时候可以简化代码
myabs = lambda x: -x if x < 0 else x
print myabs(-1)