'''
큐 자료구조 구현 (First In First Out)
: 시간 복잡도가 더 높고 비효율적으로 동작할 수 있으므로 deque 라이브러리 사용 권장
'''
from collections import deque

queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue) # 먼저 들어온 순서대로 출력 (queue)
queue.reverse() # 뒤집기
print(queue) # 나중에 들어온 원소부터 출력
