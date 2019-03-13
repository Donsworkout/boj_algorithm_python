import collections
import sys
input = sys.stdin.readline
moves = [(1,0),(-1,0),(0,1),(0,-1)]


def valid_range(a, b):
    global n
    if a >= n or b >= n or a < 0 or b < 0:
        return False
    else:
        return True


def BFS():
    c, p = 0, 0
    while queue:
        len_q = len(queue)
        for _ in range(len_q):
            cur = queue.popleft()
            x, y = cur[0], cur[1]
            for move in moves:
                cx, cy = x + move[0], y + move[1]
                if valid_range(cx, cy):
                    cha = abs(arr[cx][cy] - arr[x][y])
                    if not visited[cx][cy] and ((cha >= l) and (cha <= r)):
                        visited[cx][cy] = 1
                        varr.append((cx, cy))
                        searched[cx][cy] = 1
                        queue.append((cx, cy))
                        c += 1
                        p += arr[cx][cy]
    return c, p


n, l, r = map(int, input().split())
arr = []
super_cnt = 0
for _ in range(n):
    arr.append(list(map(int, input().split())))
while True:
    entry = []
    searched = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not searched[i][j]:
                visited = [[0]*n for _ in range(n)]
                visited[i][j] = 1
                varr = []
                varr.append((i, j))
                searched[i][j] = 1
                queue = collections.deque([(i, j)])
                cnt, p_sum = BFS()
                if cnt == 0:
                    continue
                else:
                    entry.append((int((p_sum + arr[i][j]) / (cnt + 1)), varr))
    if entry:
        for elem in entry:
            for e in elem[1]:
                arr[e[0]][e[1]] = elem[0]
        super_cnt += 1
    else:
        break

print(super_cnt)