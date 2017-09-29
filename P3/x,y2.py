import math
def f(l,angle):
    x=l*math.cos(angle)
    y=l*math.sin(angle)
    return (x,y)

x,y=f(1,math.pi/3)
print x,y

