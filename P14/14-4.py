from __future__ import division
import random
lst_number = random.sample(range(0,100),40)
print '随机数：',lst_number
sum = 0
mean = 0
for i in lst_number:
    sum = sum + i
mean = sum /40
print '总和：', sum
print '平均值：', mean
score = []
for i in lst_number:
    if i < mean:
        score.append(i)
score.sort()
print '低于平均分的为：', score