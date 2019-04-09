import sys
from collections import deque
input = sys.stdin.readline
arr = [[0] * 101 for _ in range(101)]
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

chkpoint = {}


def valid_range(a, b):
    if a < 1 or b < 1 or a > n or b > n:
        return False
    else:
        return True


def move(d):
    global cnt
    while True:
        cnt += 1
        nx, ny = body[-1][0] + dirs[d%4][0], body[-1][1] + dirs[d%4][1]
        if not valid_range(nx, ny) or ((nx, ny) in body):
            cnt += 1
            break
        body.append((nx, ny))
        if arr[nx][ny] == 1:
            arr[nx][ny] = 0
        else:
            body.popleft()
        if cnt in chkpoint:
            if chkpoint[cnt] == 'L':
                d -= 1
            else:
                d += 1
    return


n = int(input())
for _ in range(int(input())):
    r, c = map(int,input().split())
    arr[r][c] = 1
for _ in range(int(input())):
    k, v = input().split()
    chkpoint[int(k)] = v
body = deque([(1, 1)])
cnt = 0
move(0)
print(cnt-1)