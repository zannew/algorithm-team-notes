'''
[문제] 왕실의 나이트
- 왕실 정원은 체스판과 같은 8 * 8 좌표 평면이다. 왕실 정원의 특정한 한 칸에 나이트가 서있다.
- 나이트는 말을 타고 있기 때문에 이동을 할 때는 L자 형태로만 이동할 수 있으며, 정원 밖으로는 나갈 수 없다.
- 나이트는 특정 위치에서 다음과 같은 2가지 경우로 이동할 수 있다.
    1. 수평으로 두 칸 이동한 뒤에 수직으로 한 칸 이동하기
    2. 수직으로 두 칸 이동한 뒤에 수평으로 한 칸 이동하기
- 이처럼 8 * 8 좌표 평면상에서 나이트의 위치가 주어졌을 때 나이트가 이동할 수 있는 경우의 수를 출력하는 프로그램을 작성하시오.
왕실 정원에서 행 위치를 표현할 때는 1부터 8로 표현하며, 열 위치를 표현할 때는 a부터 h로 표현한다.
- ex) c2에 있을 때 이동할 수 있는 경우의 수는 6가지이다.

[키포인트]
해당 방향 벡터를 정의하고 완전탐색으로 구현
'''
import timeit

input_data = input()
start = timeit.default_timer()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) +1
# 방향 벡터 정의
steps = [(2,1),(2,-1),(1,2),(1,-2),(-2,1),(-2,-1),(-1,2),(-1,-2)]
# 결과값 선언 및 초기화
result = 0

for step in steps:
    next_row = row + step[0]
    next_column = column + step[1]
    if next_row <= 8 and next_row >= 1 and next_column <= 8 and next_column >= 1:
        result += 1

print(result)
end = timeit.default_timer()
print("%f초 걸림" % (end - start))