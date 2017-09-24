hi='''hello
python
i love you'''
f = open('hello.txt','w')
f.write(hi)
pi = f.fileno()
print pi
f.close
