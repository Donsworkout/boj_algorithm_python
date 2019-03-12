import sys
import copy
input = sys.stdin.readline
sq_moves = [(0, 0), (1, 0), (0, 1), (1, 1)]
init_move = {0: (0, 1), 1: (-1, 0), 2: (0, -1), 3: (1, 0)}
clock_move = {(0, 1):(-1, 0), (-1, 0):(0, -1), (0, -1):(1, 0), (1, 0):(0, 1)}
visited = []

def all_dragon(a,b):
    for move in sq_moves:
        if ent_arr[a+move[0]][b+move[1]] == 0:
            return False
    return True


def generator(dirt, gen):
    arr = []
    arr.append(init_move[dirt])
    if gen == 0:
        return arr
    elif gen == 1:
        arr.append(clock_move[arr[0]])
        return arr
    elif gen >= 2:
        arr.append(clock_move[arr[0]])
        cnt = 2
        while cnt <= gen:
            tmp_arr = []
            for elem in reversed(arr):
                tmp_arr.append(clock_move[elem])
            tmp_arr = arr + tmp_arr
            arr = copy.deepcopy(tmp_arr)
            cnt += 1
        return arr


ent_arr = [[0]*102 for _ in range(102)]
for _ in range(int(input())):
    x, y, d, g = map(int,input().split())
    sx, sy = x, y
    ent_arr[sy][sx] = 1
    visited.append((y,x))
    for elem in generator(d, g):
        sy = sy + elem[0]
        sx = sx + elem[1]
        ent_arr[sy][sx] = 1
        visited.append((sy, sx))

cnt = 0
for i in range(101):
    for j in range(101):
        if all_dragon(i, j):
            cnt += 1
print(cnt)