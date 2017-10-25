class Printer(object):
    def __init__(self,val):
        self.val = val
    def __repr__(self):
        return str(self.val)
objs = [Printer(2),Printer(3)]
for x in objs:
  print (x)
  print (objs)