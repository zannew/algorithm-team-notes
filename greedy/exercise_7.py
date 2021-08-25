'''
백준 > 그리디 > 컵라면
링크 : https://www.acmicpc.net/problem/1781
'''
import heapq
import sys

read = sys.stdin.readline

n = int(read().strip("\n"))
problems = list()

for i in range(n):
    deadline, ramen = map(int, read().strip("\n").split())
    problems.append((deadline, ramen))

problems.sort()
print(problems)

queue = []

for problem in problems:
    heapq.heappush(queue, problem[1])
    print(queue)
    print("len(queue) = ", len(queue))
    if problem[0] < len(queue):
        heapq.heappop(queue)

print(sum(queue))