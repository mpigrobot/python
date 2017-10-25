#!/usr/bin/python
# -*- coding: utf-8 -*-
import time          #调用函数模块
def performance(f):   #定义装饰器函数
    def fn(*args, **kw):   #定义接收任何参数的子函数
        t1 = time.time()    #获取当前电脑时间
        r = f(*args, **kw)    #传入并运行factorial()函数
        t2 = time.time()       #获取当前电脑时间
        print 'call %s()in %fs' % (f.__name__, (t2 - t1))
        return r
    return fn

@performance
def factorial(n):
    return reduce(lambda x,y: x*y, range(1, n+1))
print factorial(10)

# %s 输出一个字符串
# %FS的意思是指精度和满量程的百分比
# 第一行，导入模块time
# 第二行，定义一个叫performance的函数，接收一个参数
# 第三行，定义一个函数，接收任何参数
# 第四行，调用time模块的time方法，得到系统当前时间的时间戳
# 第五行，调用函数f，这个f函数就是传递给performance函数的参数，且f函数接收任何参数
# 第六行，再次调用time模块的time方法，获得当前时间的时间戳
# 第七行，打印调用的函数名，和调用函数的前后时间差（用到了字符串的占位符，可看一下python中的格式化字符串）
# 第八行，返回f函数的调用结果
# 第九行，返回新定义的函数fn
# 综上：函数performance接收一个函数作为参数，对这个函数进行包装，返回一个新函数