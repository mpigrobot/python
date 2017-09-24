filename = raw_input('Enter file name: ')
f = open(filename,'r')
for eachline in f:
    print eachline,
f.close()
