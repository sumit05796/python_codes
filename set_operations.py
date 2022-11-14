s = {10,20,30}

#adds element x to set#
s.add(40)
print(s)

#removes all elements from the set#
s.clear()
print(s)

#Returns a shallow copy of set#
s = {10,20,30}
s.copy()
print(s.copy())

#Returns the element present in set  but not in set s1 as a new set#
s = {10,20,30}
s1 = {20,30,40}
s.difference(s1)
print(s.difference(s1))

#removes all elements in set s1 from the original set#
s = {10,20,30}
s1 = {20,30,40}
s.difference_update(s1)
print(s.difference_update(s1))

#removes the element x from the set, if present#
s = {10,20,30}
s.discard(30)
print(s)

#returns the common elements as new set from two given sets#
s = {10,20,30}
s1 = {20,30,40}
s.intersection(s1)
print(s.intersection(s1))

#updates the intersected elemnets of itself and another set s1#
s = {10,20,30}
s1 = {20,30,40}
s.intersection_update(s1)
print(s.intersection_update(s1))

#Returns TRUE if two sets have no common elements#
s = {10,20,30}
s1 = {50,40}
s.isdisjoint(s1)
print(s.isdisjoint(s1))

#Returns TRUE if given set is a subset of set s1#
s = {10,20,30}
print(s.issubset({10,20,30,40}))

#Returns TRUE if s1 is a subset of given set#
s = {10,20,30}
print(s.issuperset({10,20}))

#returns and removes an arbitrary set element#
s = {10,20,30}
print(s.pop())

#removes the element x from set#
s = {10,20,30}
s.remove(20)
print(s)

#Returns the symmetric difference elements of original set  as new set#
s = {10,20,30}
print(s.symmetric_difference({20,30}))

#Updates a set  with symmetric difference of itself and s1#
s = {10,20,30}
print(s.symmetric_difference_update({20,30}))

#Returns UNION of sets as new set#
s = {10,20,30}
s1 = {20,30}
s.union(s1)
print(s)

#Update the set with union of itself and s1#
s = {10,20,30}
s1 = {20,30}
s.update(s1)
print(s)
