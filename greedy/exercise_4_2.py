'''
백준 > 그리디 > 컵홀더
링크 : https://www.acmicpc.net/problem/2810
'''
n = int(input())
seats = input()
s_count = seats.count("S")
ll_count = seats.count("LL")
result = 0

if ll_count >= 1:
    result = s_count + ll_count + 1
else:
    result = s_count

print(result)