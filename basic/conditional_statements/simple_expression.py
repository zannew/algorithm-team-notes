# coding simply 1
score = 85

if score >= 80 : result = "success"
else : result = "foil"

print(result)

# coding simply 2
score = 75
result = "success" if score >= 80 else "fail"

print(result)

# coding simply 3
a = [1, 2, 3, 4, 5, 5, 5]
remove_set = {3, 5}

result = [i for i in a if i not in remove_set]
print(result)

