
def average(*args):
    sum=0.0
    if len(args)==0:
        return 0.0
    for x in args:
        sum=sum+x
    return(sum/len(args))
print average(1, 2, 3, 4)
