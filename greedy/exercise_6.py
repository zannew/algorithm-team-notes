'''
백준 > 그리디 > 사과 담기 게임
링크 : https://www.acmicpc.net/problem/2828
'''
n, m = map(int, input().split())
j = int(input())
count = 0
start = 1
end = m

for _ in range(j):
    p = int(input())
    if p > end:
        count += (p - end)
        start += (p - end)
        end = p
    elif p < start:
        count += (start - p)
        end -= (start - p)
        start = p

print(count)