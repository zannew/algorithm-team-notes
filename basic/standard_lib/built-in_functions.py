# available functions without importing
result = sum([1,2,3,4,5])
print(result)

result = min([1,2,3,4,5])
print(result)

result = max([1,2,3,4,5])
print(result)

result = eval("(3 + 5) * 7")
print(result)

result = sorted([9, 1, 8, 5, 4])
print(result)
result = sorted([9, 1, 8, 5, 4], reverse=True)
print(result)

result = sorted([('Joy', 35),('Paul', 75),('Peter', 50)], key = lambda x: x[1], reverse = True)
print(result)

data = [9, 1, 8, 5, 4]
data.sort(reverse=True)
print(data)
data.sort()
print(data)