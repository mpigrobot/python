#!/usr/bin/python
# -*- coding: utf-8 -*-
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def __str__(self):
        return '(%s: %s)' % (self.name, self.score)
    __repr__ = __str__

    def __cmp__(self, s):
        if self.name < s.name:
            return -1
        elif self.name > s.name:
            return 1
        else:
            return 0

L = [Student('Tim', 99), Student('Bob', 88), Student('Alice', 77),100,'Hello,MPIG']
print sorted(L)
# 上述 Student 类实现了__cmp__()方法，__cmp__用实例自身self和传入的实例 s 进行比较，
# 如果 self 应该排在前面，就返回 -1，如果 s 应该排在前面，就返回1，如果两者相当，返回 0。