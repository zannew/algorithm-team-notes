'''
[문제] 큰 수의 법칙 :
다양한 수로 이루어진 배열이 있을 때 주어진 수들을 M번 더하여 가장 큰 수를 만드는 법칙이다. 단, 배열의 특정한 인덱스(번호)에 해당하는 수가 연속해서 K번을 초과하여
더해질 수 없는 것이 이 법칙의 특징이다.
단, 서로 다른 인덱스에 해당하는 수가 같은 경우에도 서로 다른 수라고 간주한다.
첫째줄에 배열의 크기 N, 숫자가 더해지는 횟수 M, 그리고 K가 주어지고 둘째줄에 배열의 숫자가 입력될 때 이 큰 수의 법칙에 다른 결과를 출력하시오.

* 5_2에서는 반복되는 수열에 대해 파악하는 것이 핵심!

'''
n, m, k = map(int, input().split())
data = list(map(int, input().split()))
data.sort()

result = 0
count = 0 # 최종적으로 first가 더해질 횟수

first = data[n - 1]
second = data[n - 2]

# first가 더해질 횟수를 구한다.
count = int(m / (k + 1)) * k
count += m % (k + 1)

result += count * first
result += (m - count) * second


print(result)

