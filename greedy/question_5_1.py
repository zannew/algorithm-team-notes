'''
[문제] 큰 수의 법칙 :
다양한 수로 이루어진 배열이 있을 때 주어진 수들을 M번 더하여 가장 큰 수를 만드는 법칙이다. 단, 배열의 특정한 인덱스(번호)에 해당하는 수가 연속해서 K번을 초과하여
더해질 수 없는 것이 이 법칙의 특징이다.
단, 서로 다른 인덱스에 해당하는 수가 같은 경우에도 서로 다른 수라고 간주한다.
첫째줄에 배열의 크기 N, 숫자가 더해지는 횟수 M, 그리고 K가 주어지고 둘째줄에 배열의 숫자가 입력될 때 이 큰 수의 법칙에 다른 결과를 출력하시오.
'''
n, m, k = map(int, input().split())
data = list(map(int, input().split()))
data.sort()

result = 0
count = 0

for _ in range(m):
    count += 1
    if count > k:
        result += data[-2] # count가 k와 같아지면 두번째로 큰 수를 더하고 count를 초기화한다.
        count = 0
    else:
        result += data[-1] # count가 채워지지 않은 상태이면 가장 큰 수를 계속 더한다.

print(result)

