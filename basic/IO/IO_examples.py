# IO example 1
n = int(input())

# add elements without space
data = list(map(int, input().split()))
data.sort(reverse = True)

print(data)

# IO example 2
n, m, k = map(int, input().split())

print(n, m, k)