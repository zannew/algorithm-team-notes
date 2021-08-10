'''
 how to initialize : one-dimensional
'''
# array 1
array = [i for i in range(10) if i % 2 == 1]

print(array)

# array 2
array = []

for i in range(10):
    if i % 2 == 1:
        array.append(i)

print(array)

# each part of arrays results the same.

'''
 how to initialize : two-dimensional
'''
n = 3
m = 4

# 1. list comprehension
arrays = [[0] * m for _ in range(n)]
print(arrays)

arrays = []

# 2. 잘못된 초기화 : 생성되는 3개의 리스트가 모두 동일한 객체에 대한 레퍼런스로 인식
arrays = [[0] * m] * n
print(arrays)

# 1과 2의 초기화 방법에 따라 결과가 다르다.
arrays[1][1] = 5
print(arrays)
