hi='''hello
python
i love you'''
f = open('hello.txt','w')
f.write(hi)
f = open('hello.txt','r')
pi = f.fileno()
print pi
f.close
