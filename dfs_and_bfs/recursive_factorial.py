'''
팩토리얼 예제
- n! = 1 * 2 * 3 * ... * (n-1) * n
- 수학적으로 0!과 1!의 값은 1
'''

def factorial_iterative(i):
    result = 1
    for i in range(1, i+1):
        result *= i
    return result

def factorial_recursive(i):
    if i <= 1:
        return 1
    return i * factorial_recursive(i - 1)

print("반복적으로 구현 : ", factorial_iterative(5))
print("재귀적으로 구현 : ", factorial_recursive(5))