'''
백준 > 그리디 > 거스름돈
링크 : https://www.acmicpc.net/problem/5585
'''
n = 1000 - int(input())
count = 0
coin_types = [500, 100, 50, 10, 5, 1]

for coin in coin_types:
    count += n // coin
    n %= coin

print(count)

