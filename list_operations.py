#ADD element x to end of the list#
list_1 = [10,20,30]
list_1.append(40)
print(list_1)

#Removes all the elements from the list#
list_1.clear()
print(list_1)

#Returns the shallow copy of the list#
list_1 = [10,20,30]
list_1.copy()
print(list_1)

#returns the no of occurences of element x in the list#
print(list_1.count(10))

#extends the list with elements of iterable y#
y = [40,50]
list_1.extend(y)
print(list_1)

#returns the index of first occurence of element x in list#
list_1.index(20)
print(list_1.index(30))

#Insert element x before i in the list#
list_1.insert(1,11)
print(list_1)

#Removes the item at index i and returns the item#
list_1.pop(1)
print(list_1)

#Remove the first occurence of element x from list#
list_1.remove(50)
print(list_1)

#reverse the elements in the list#
list_1.reverse()
print(list_1)

#sorts the elements in ascending order#
list_1.sort()
print(list_1)