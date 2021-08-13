'''
[문제] 1이 될 때까지 : 어떠한 수 N이 1이 될 때까지 다음 중 두 과정 중 하나를 반복적으로 수행하려고 한다. 단, 2번째 연산은 N이 K로 나누어 떨어질 때만 선택할 수 있다.
1. N에서 1을 뺀다.
2. N에서 K를 나눈다.

과정을 수행해야 하는 최소 횟수를 구하는 문제
아래 풀이는 시간복잡도 O(logN)의 로그시간이 걸림
'''

n, k = map(int, input().split())

result = 0

while True:
    target = (n // k) * k
    result += (n - target)
    n = target
    if n < k:
        break
    result += 1
    n //= k

result += (n - 1)
print(result)

