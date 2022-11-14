dict_1= {1:'xyz', 2:'pqr', 3:'abc'}

#Remove all items from dictionary#
dict_1.clear()
print(dict_1)

#A shallow of dictionary is created#
dict_1 = {1:'xyz', 2:'pqr', 3:'abc'}
dict_1.copy()
print(dict_1)

#Creates a new dictionary from values of an iterable as keys#
print(dict_1.fromkeys([2,3]))

#Gets the value for the key x, if x is present , esle default#
print(dict_1.get(3))

#get a set like view of elements of dictionary#
print(dict_1.items())

#Gives a set like view of the keys# in dictionary#
print(dict_1.keys())

#Removes the values corresponding to key x , if present#
print(dict_1.pop(2))

#Removes and returns some (key,value) pair#
print(dict_1.popitem())

#Insert default value v against key k, if k is not present#
dict_1.setdefault(2,'jkl')
print(dict_1)

#updates dictionary with the key-values pair  of another dictionary#
dict_1 = {1:'xyz', 2:'pqr', 3:'abc'}
dict_2 = {3:'efg', 4:'hij'}
dict_1.update(dict_2)
print(dict_1)

#Gives a set view of all the values in dictionary#
print(dict_1.values())