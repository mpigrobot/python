import math
def f(l,angle):
    x=l*math.cos(angle)
    y=l*math.sin(angle)
    return (x,y)

r=f(1,math.pi/3)
x,y=f(1,math.pi/3)
print x,y
print(r)

    
