from __future__ import division
import random

def make_score(num):
    score = [random.randint(0,100) for i in range(num)]
    return score

def less_average(score):
    num = len(score)
    sum_score = sum(score)
    ave_num = sum_score//num
    less_ave = [i for i in score if i<ave_num]
    return len(less_ave)

if __name__=="__main__":
    score = make_score(40)
    print "the number of less average is:",less_average(score)
    print "the every socre is[from big to small]:",sorted(score,reverse=True)