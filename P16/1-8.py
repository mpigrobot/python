#!/usr/bin/env python
# coding:utf-8

import sys
sys.path.append("../")
import jieba
jieba.load_userdict( 'C:\Users\Administrator\Desktop\dir1.txt')
print ", ".join(jieba.cut("江州市长江大桥参加了长江大桥的通车仪式"))
# jieba.suggest_freq('江大桥', True)
jieba.add_word("江大桥", freq = 20000, tag = None)
print ", ".join(jieba.cut("江州市长江大桥参加了长江大桥的通车仪式"))
