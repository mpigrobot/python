import bisect
a=[1,2,3,4,5,6,7,8,9]
b=[1,2,3,5,7,8,9,0]
m=bisect.bisect_left(a,4)
n=bisect.bisect_left(b,6)
q=bisect.bisect_left(b,6,2,7)
print m,n,q