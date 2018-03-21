#!/usr/bin/env python
# coding:utf-8

import sys
sys.path.append("../")
import jieba
print ", ".join(jieba.cut("大连美容美发学校中君意是你值得信赖的选择"))
jieba.load_userdict( 'C:\Users\Administrator\Desktop\dir1.txt')
print ", ".join(jieba.cut("大连美容美发学校中君意是你值得信赖的选择"))
# jieba.suggest_freq('君意', True)
jieba.add_word("君意", freq = 20000, tag = None)
print ", ".join(jieba.cut("大连美容美发学校中君意是你值得信赖的选择"))