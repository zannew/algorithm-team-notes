import heapq

def heapsort(iterable):
    h = []
    result = []
    # add all elements on heap
    for value in iterable:
        heapq.heappush(h, value)
    print("h : ", h)
    # get one element by one from heap
    for _ in range(len(h)):
        result.append(heapq.heappop(h))
    return result

result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result)

