import collections
import sys
input = sys.stdin.readline
moves = [(1,0),(-1,0),(0,1),(0,-1)]

def nice_range(m,k):
    if m < 0 or k < 0 or m >= n or k >= n:
        return False
    else:
        return True

def feed_finder(a,b,w):
    queue = collections.deque([(a, b, 0)])
    entry = []
    visited = [[0] * n for _ in range(n)]
    filter_status = False
    result_d = -999
    while queue:
        len_q = len(queue)
        for _ in range(len_q):
            cur = queue.popleft()
            x, y, cur_d = cur[0], cur[1], cur[2]
            if arr[x][y] != 0 and arr[x][y] < w:
                if ((filter_status == True) and (cur_d == result_d)) or filter_status == False:
                    filter_status = True
                    result_d = cur_d
                    entry.append((x, y))
            if filter_status == False:
                for move in moves:
                    mx, my = x + move[0], y + move[1]
                    if nice_range(mx, my):
                        if arr[mx][my] <= w and not visited[mx][my]:
                            queue.append((mx, my, cur_d + 1))
                            visited[mx][my] = 1
    if entry:
        return sorted(entry)[0], result_d
    else:
        return [], result_d


n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int,input().split())))
    for j in range(n):
        if arr[i][j] == 9:
            shark_pos = (i, j)
            arr[i][j] = 0
time_v = 0
weight = 2
mari = 0
sp_x, sp_y = shark_pos[0], shark_pos[1]

while True:
    target, to_dst = feed_finder(sp_x, sp_y, weight)
    if not target:
        break
    else:
        mari += 1
        if mari == weight:
            weight += 1
            mari = 0
        time_v += to_dst
        arr[target[0]][target[1]] = 0
        sp_x, sp_y = target[0], target[1]

print(time_v)
