import collections
import sys
import copy

input = sys.stdin.readline
moves = [(1,0),(-1,0),(0,1),(0,-1)]

def valid_range(a,b):
    global n,m
    if a >= n or b >=m or a < 0 or b < 0:
        return False
    else:
        return True

def bfs(l, q, v):
    while q:
        len_q = len(q)
        for _ in range(len_q):
            cur = q.popleft()
            x, y = cur[0], cur[1]
            for move in moves:
                mx, my = x + move[0], y + move[1]
                if valid_range(mx,my) and not v[mx][my] and l[mx][my] == 0:
                    l[mx][my] = 1
                    q.append((mx, my))
                    v[mx][my] = 1
    s = 0
    for i in range(n):
        s += l[i].count(0)
    return s

n,m = map(int,input().split())
lab = []
defender = []
queue = collections.deque([])
visited = [[0]*m for rows in range(n)]
for i in range(n):
    lab.append(list(map(int,input().split())))
    for j in range(m):
        if lab[i][j] == 2:
            queue.append((i, j))
            visited[i][j] = 1
        if lab[i][j] == 0:
            defender.append((i,j))
max_v = 0
for i in defender:
    for j in defender:
        for k in defender:
            if i == j or j == k or k == i:
                continue
            l = copy.deepcopy(lab)
            q = collections.deque(list(queue))
            v = copy.deepcopy(visited)

            l[i[0]][i[1]] = 1
            l[j[0]][j[1]] = 1
            l[k[0]][k[1]] = 1
            tmp = bfs(l, q, v)
            if max_v < tmp:
                max_v = tmp
print(max_v)