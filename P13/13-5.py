class Students(object):
    def __init__(self, *args):
        self.name = args
    def __len__(self):
        return len(self.name)
ss = Students('Bob', 'Alice', 'Tim')
print len(ss)