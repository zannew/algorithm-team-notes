i = 1
result = 0

while i <= 9 :
    result += i
    i += 1

print(result)

# add only odd number
i = 1
result = 0

while i <= 9 :
    if i % 2 != 0 :
        result += i
    i += 1

print(result)