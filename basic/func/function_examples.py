# func 1
def add(a, b):
    print('result : ', a+b)

add(1,2)

# func 2
a = 0

def func():
    global a
    a += 1

for i in range(10):
    func()

print('a : ', a)
