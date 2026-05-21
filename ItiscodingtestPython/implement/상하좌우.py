'''N = int(input())
move_list = list(map(str, input().split()))
x = 1
y = 1

def up(x, y):
    if x - 1 > 0:
        x = x - 1
    return x

def down(x, y):
    # 공간 크기 N을 포함할 수 있도록 <= N으로 수정
    if x + 1 <= N:
        x = x + 1
    return x

def left(x, y):
    if y - 1 > 0:
        y = y - 1
    return y

def right(x, y):
    # 공간 크기 N을 포함할 수 있도록 <= N으로 수정
    if y + 1 <= N:
        y = y + 1
    return y

print(f"시작 위치: ({x}, {y})")

for move in move_list:
    prev_x, prev_y = x, y

    # 잘못된 매핑 수정: D는 x축 증가, L은 y축 감소
    if move == 'U':
        x = up(x, y)
    elif move == 'D':
        x = down(x, y)
    elif move == 'L':
        y = left(x, y)
    elif move == 'R':
        y = right(x, y)
    
    print(f"이동 명령: {move} | ({prev_x}, {prev_y}) -> ({x}, {y})")

print(f"최종 결과: {x} {y}")'''

n = int(input())
x, y = 1, 1
plans = input().split()

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x, y = nx, ny

print(x,y)