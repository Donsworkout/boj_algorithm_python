import collections
from itertools import combinations
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
    count = 0
    while queue:
        len_q = len(queue)
        for _ in range(len_q):
            cur = queue.popleft()
            x,y = cur[0],cur[1]
            if chk_arr[x][y] == 2:
                return count
            for move in moves:
                if valid_range(x+move[0],y+move[1]) and not visited[x+move[0]][y+move[1]]:
                    queue.append((x+move[0],y+move[1]))
                    visited[x+move[0]][y+move[1]] = 1
        count += 1


arr = []
chicken_pos = []
house_pos = []
min_arr = []
n,m = map(int,input().split())
for i in range(n):
    arr.append(list(map(int,input().split())))
    for j in range(n):
        if arr[i][j] == 2:
            chicken_pos.append((i, j))
        elif arr[i][j] == 1:
            house_pos.append((i, j))
for case in list(combinations(chicken_pos,m)):
    chk_arr = [[0]*n for _ in range(n)]
    for pos in chicken_pos:
        chk_arr[pos[0]][pos[1]] = 0
    for e in case:
        chk_arr[e[0]][e[1]] = 2
    cnt = 0
    for house in house_pos:
        visited = [[0]*n for _ in range(n)]
        visited[house[0]][house[1]] = 1
        queue = collections.deque([house])
        cnt += BFS()
    min_arr.append(cnt)
print(min(min_arr))