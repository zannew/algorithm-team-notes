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

# counting
print("number of data which values of 3 : ", a.count(3))

# removes the first matching element
a.remove(3)
print("removed : ", a)