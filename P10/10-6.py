#!/usr/bin/python
# -*- coding: utf-8 -*-
# 匿名函数有个限制，就是只能有一个表达式，不写return，返回值就是该表达式的结果。
print filter(lambda s: s and len(s.strip()) > 0, ['test', None, '', 'str', '  ', 'END'])

def is_not_empty(s):
     return s and len(s.strip()) > 0
print filter(is_not_empty, ['test', None, '', 'str', '  ', 'END'])