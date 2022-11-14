import array as arr
a = arr.array('I', [2,5,10,12,6,7])
print(a)

#type of array elements#
print(a.typecode)

#returns the bytes occupied#
print(a.itemsize)

#append value of x to end of array#
x = 11
a.append(x)
print(a)

#buffer i.e. return first address of array and no. of elements in array#
print(a.buffer_info())

# No. of occurences of element x in an array#
print(a.count(6))

#append elelments of y to end of the array,  y is same type of array as a otherwise raise TypeError#
y = [20,30,40]
a.extend(y)
print(a)

#returns first occurence index of x in array#
print(a.index(6))

#Insert element x into array at index i and shifts the array elemnts to next index#
a.insert(3,4)
print(a)

#Returns the element at index i and deletes the element at that index from array#
a.pop(8)
print(a)

#Deletes the first occurence of element x in the array#
a.remove(11)
print(a)

#Reverses the order of the array elements#
a.reverse()
print(a)

#convert array elemnts to array of machine values and returns the byte representation#
print(a.tobytes())

#Converts the array elemnets into a normal list#
a.tolist()
print(a.tolist())

#Writes the array elements as machine values to file object f #
a.tofile(f)


