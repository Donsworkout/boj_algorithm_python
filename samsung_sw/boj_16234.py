from collections import deque
import sys
input = sys.stdin.readline
dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def valid_range(a, b):
    if a < 0 or b < 0 or a >=n or b >=n:
        return False
    else:
        return True


def BFS():
    global switch
    while(queue):
        len_q = len(queue)
        for _ in range(len_q):
            cur = queue.popleft()
            cx, cy = cur[0], cur[1]
            for d in dirs:
                dx, dy = cx + d[0], cy + d[1]
                if valid_range(dx, dy) and not covered[dx][dy]:
                    cha = abs(arr[dx][dy] - arr[cx][cy])
                    if cha >= l and cha <= r:
                        covered[dx][dy] = 1
                        visited.append((dx, dy))
                        queue.append((dx, dy))
                        switch = True
    return


arr = []
n, l, r = map(int, input().split())
for _ in range(n):
    arr.append(list(map(int, input().split())))

cnt = 0
while True:
    switch = False
    all_parts = []
    covered = [[0]*50 for _ in range(50)]
    for i in range(n):
        for j in range(n):
            covered[i][j] = 1
            visited = [(i, j)]
            queue = deque([(i, j)])
            BFS()
            if len(visited) > 1:
                all_parts.append(visited)
    for part in all_parts:
        sum_v = 0
        for elem in part:
            sum_v += arr[elem[0]][elem[1]]
        val = sum_v // len(part)
        for elem in part:
            arr[elem[0]][elem[1]] = val
    if not switch:
        break
    cnt += 1
print(cnt)