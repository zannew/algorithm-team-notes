a = []
b = []
value = 3

for i in range(0, 200):
    a.append(value * i)

for i in range(0, 200):
    b.append(a[199 - i])


print(b[0])
print(b[199])

print(a[0:10:2])
print(b[-1:-10:-2])
print(a[0:10:1])
print(b[-1:-10:-1])


print((2//0)*0)