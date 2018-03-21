from bintrees import *
btree = BinaryTree()
btree.__setitem__("Tom","headmaster")
print btree
adict = [(2,"phone"),(5,"tea"),(9,"scree"),(7,"computer")]
btree.update(adict)
print btree
print btree.__contains__(5)
print btree.__contains__("qiwsir")
btree.__delitem__(5)
print btree
print btree.__getitem__("Tom")
aiter = btree.__iter__()
print aiter.next()
print aiter.next()
print btree.__len__()
print btree.__max__()
print btree.__min__()
other = [(3,'http://blog.csdn.net/qiwsir'),(7,'computer')]
bother = BinaryTree()
bother.update(other)
print btree.__and__(bother)
print btree.__or__(bother)
print btree.__sub__(bother)
print btree.__xor__(bother)
for (k,v) in btree.items():
   print k, v
for v in btree.values():
   print v
for (k,v) in btree.items(reverse=True):
   print k,v
for (k, v) in btree.iter_items(6, 9):
    print k, v
ctree = btree.copy()
print ctree.pop(2)
print btree.set_default(7)
btree.set_default(3.13,"gmj")
print btree
