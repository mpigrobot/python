f=open('hello.txt')  
while True:
    l=f.readline()    
    if len(l)==0:     
        break
    print(l)
