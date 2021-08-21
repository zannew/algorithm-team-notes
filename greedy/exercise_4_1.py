'''
백준 > 그리디 > 컵홀더
링크 : https://www.acmicpc.net/problem/2810
'''
n = int(input())
seats = input()
s_count, l_count = 0
result = 0

for seat in seats:
    if seat == "S":
        s_count += 1
    else:
        l_count += 1

if l_count >= 1:
    result = s_count + (l_count // 2) + 1
else:
    result = s_count

print(result)