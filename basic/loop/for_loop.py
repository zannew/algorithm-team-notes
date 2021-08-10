result = 0

# 1 ~ 9
for i in range(1, 10) :
    result += i

print(result)

result = 0

# 0 ~ 9
for i in range(10) :
    result += i

print(result)

scores = [90, 85, 77, 65, 97]

for i in range(len(scores)) :
    if scores[i] >= 80 :
        print(i + 1, "번 합격")



# continue

scores = [90, 85, 77, 65, 97]
cheating_list = {2, 4}

for i in range(len(scores)) :
    if i+1 in cheating_list :
        continue
    if scores[i] >= 80 :
        print(i+1, "번 합격")


# nested for loop : Normally used in Floyd–Warshall algorithm, Dynamic programming
for i in range(2, 10) :
    for j in range(1, 10) :
        print(i, "x", j, "=", i*j)
    print()

