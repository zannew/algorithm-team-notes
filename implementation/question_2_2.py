'''
[문제] 시각
정수 N이 입력되면 00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수를 구하는 프로그램을 작성하시오.

예를 들어 1을 입력했을 때 다음은 3이 하나라도 포함되어 있으므로 세어야 하는 시각이다.
- 00시 00분 03초
- 00시 13분 30초

반면에 다음은 3이 하나도 포함되어 있지 않으므로 세면 안 되는 시각이다.
- 00시 02분 55초
- 01시 27분 45초

[키포인트]
가능한 모든 시각의 경우를 하나씩 모두 세서 풀 수 있는 문제
'''
import timeit

n = int(input())
count = 0
start = timeit.default_timer()

def check(i, j, k):
    if i % 10 == 3 or j // 10 == 3 or j % 10 == 3 or k // 10 == 3 or k % 10 == 3 :
        return True
    else:
        return False

for i in range(n + 1):
    for j in range(60):
        for k in range(60):
            if check(i, j, k):
                count += 1

print(count)

end = timeit.default_timer()
print("%f초 걸림" % (end - start))