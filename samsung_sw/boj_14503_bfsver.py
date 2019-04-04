import sys
from collections import deque
input = sys.stdin.readline

moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]
left_of = {0: 3, 1: 0, 2: 1, 3: 2}
back_of = {0: 2, 1: 3, 2: 0, 3: 1}
arr = []


def valid_range(a, b):
    if a < 0 or b < 0 or a >= n or b >= m:
        return False
    else:
        return True


def bfs():
    global cnt
    while queue:
        len_q = len(queue)
        for _ in range(len_q):
            cur = queue.popleft()
            cy, cx, cd = cur[0], cur[1], cur[2]
            nd = cd
            switch = True
            for _ in range(4):
                nd = left_of[nd]
                ny, nx = cy + moves[nd][0], cx + moves[nd][1]
                if valid_range(ny, nx) and not visited[ny][nx] and arr[ny][nx] == 0:
                    visited[ny][nx] = 1
                    cnt += 1
                    queue.append((ny, nx, nd))
                    switch = False
                    break
            if switch:
                nd = back_of[cd]
                ny, nx = cy + moves[nd][0], cx + moves[nd][1]
                if valid_range(ny, nx) and arr[ny][nx] == 0:
                    queue.append((ny, nx, cd))


n, m = map(int, input().split())
r, c, d = map(int, input().split())
for _ in range(n):
    arr.append(list(map(int, input().split())))

visited = [[0] * m for _ in range(n)]
queue = deque([(r, c, d)])
visited[r][c] = 1
cnt = 1
bfs()
print(cnt)