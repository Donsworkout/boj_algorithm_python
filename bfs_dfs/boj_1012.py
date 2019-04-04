import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)
moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def 정상범위(y, x):
    if x < 0 or y < 0 or x >= m or y >= n:
        return False
    else:
        return True


def 밭헤집기(y, x):
    방문[y][x] = 1
    for move in moves:
        my, mx = y + move[0], x + move[1]
        if 정상범위(my, mx) and not 방문[my][mx] and 배추있니[my][mx]:
            밭헤집기(my, mx)



t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split())
    배추위치 = []
    방문 = [[0]*m for _ in range(n)]
    배추있니 = [[0]*m for _ in range(n)]
    for _ in range(k):
        x, y = map(int, input().split())
        배추위치.append((y, x))
        배추있니[y][x] = 1
    cnt = 0
    for 좌표 in 배추위치:
        if not 방문[좌표[0]][좌표[1]]:
            밭헤집기(좌표[0], 좌표[1])
            cnt += 1
    print(cnt)