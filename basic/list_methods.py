a = [1, 4, 3]
print("basic list : ", a)

# appends an element
a.append(2)
print("appended : ", a)

# sort : asc
a.sort()
print("sorted asc : ", a)

# sort : desc
a.sort(reverse = True)
print("sorted desc : ", a)

# reverse
a.reverse()
print("reverse : ", a)

# adding data to a specific index
a.insert(2, 3)
print("added 3 at 2 : ", a)

a. insert(len(a), 7)
print("added 7 at the end: ", a)

# counting
print("number of data which values of 3 : ", a.count(3))

# removes the first matching element
a.remove(3)
print("removed : ", a)

# removes the all of matching elements
remove_set = [3, 7]

# Result has values not in "remove_set"
result = [i for i in a if i not in remove_set]
print("result : ", result)
