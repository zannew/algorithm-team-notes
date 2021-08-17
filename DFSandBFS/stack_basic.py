'''
스택 자료구조 구현 (Last In First Out)

'''

list = []

list.append(5)
list.append(2)
list.append(3)
list.append(7)
list.pop()
list.append(1)
list.append(4)
list.pop()

print(list[::-1])
print(list)