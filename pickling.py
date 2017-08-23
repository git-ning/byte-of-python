#!/usr/bin/python

# pickle，使用该模块你可以将任意对象存储在文件中，
# 之后又可以将其完整的取出来。
# 这被称为持久地存储对象

import pickle

shoplistfile = 'shoplist.data'
shoplist = ['apple', 'mango', 'carrot']
print(shoplist)

# write to the file
f = open(shoplistfile, 'wb')
pickle.dump(shoplist, f)    # dump the object to a file
f.close()

del shoplist    # detroy the shoplist variable
# print(shoplist)

# Read back from the storage
f = open(shoplistfile, 'rb')
storedlist = pickle.load(f)
print(storedlist)