def ahead_one():
    a = [i+1 for i in range(10)]
    # a = [1,2,3,4,5,6,7,8,9,10]
    b = a.pop(0)
    a.append(b)
    return a

if __name__ =="__main__":
    print ahead_one()