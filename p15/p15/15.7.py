from bisect import *

def bisectSearch(lst, x):
    i = bisect_left(lst, x)
    if i != len(lst) and lst[i] == x:
        return i
    raise ValueError

if __name__=="__main__":
    lst = sorted([2,5,3,8])
    print bisectSearch(lst,5)