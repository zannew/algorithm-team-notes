'''
[문제] 상하좌우 : 여행가 A는 N * N 크기의 정사각형 공간 위에 서 있다. 이 공간은 1 * 1 크기의 정사각형으로 나누어져있다. 가장 왼쪽 위 좌표는 (1,1)이며,
가장 오른쪽 아래 좌표는 (n,n)에 해당한다. 여행가 A는 상, 하, 좌, 우 방향으로 이동할 수 있으며, 시작 좌표는 항상 (1,1)이다. 우리 앞에는 여행가 A가 이동할
계획이 적힌 계획서가 놓여있다.
계획서에는 하나의 줄에 띄어쓰기를 기준으로 하여 L, R, U, D 중 하나의 문자가 반복적으로 적혀있다. 각 문자의 의미는 다음과 같다.
- L : 왼쪽으로 한 칸 이동
- R : 오른쪽으로 한 칸 이동
- U : 위로 한 칸 이동
- D : 아래로 한 칸 이동

'''
# R U L D
# 방향 벡터 정의
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

n = int(input())
# 시작 좌표
x, y = 1, 1
plans = list(map(str, input().split()))
# 우 상 좌 하 -> 방향 타입 리스트 생성
move_types = ['R','U','L','D']

# 입력받은 계획서로 반복문을 만든다.
for plan in plans:
    # 방향 타입을 체크하는 반복문을 만든다.
    for i in range(len(move_types)):
        # 입력받은 계획서대로 순서대로 방향 타입과 맞는지 비교한다.
        if plan == move_types[i]:
            # 입력받은 계획에 해당하는 값과 타입이 같으면 미리 만들어둔 이동값 리스트의 인덱스 값만큼 x, y 좌표를 이동해준다.
            nx = x + dx[i]
            ny = y + dy[i]
    # 이동한 값이 1보다 작거나 주어진 값보다 커져버린 경우에는 continue로 실제 x,y의 값에 저장하지 않고 지나친다.
    if nx < 1 or nx > n or ny < 1 or ny > n:
        continue
    x, y = nx, ny

print(x, y)
