'''
백준 > 그리디 > 한조서열정리하고옴ㅋㅋ
링크 : https://www.acmicpc.net/problem/14659
'''
n = int(input())
summits = list(map(int, input().split()))
current_max = 0
max_count = 0
count = 0

for summit in summits:
    if current_max < summit:
        current_max = summit
        count = 0
    else:
        count += 1

    max_count = max(max_count, count)

print(max_count)