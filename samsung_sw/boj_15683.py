import sys
import copy
input = sys.stdin.readline

d = {1: [[(0, 1)], [(1, 0)], [(0, -1)], [(-1, 0)]],
     2: [[(0, 1), (0, -1)], [(1, 0), (-1, 0)]],
     3: [[(0, 1), (1, 0)],
        [(1, 0), (0, -1)],
        [(0, -1), (-1, 0)],
        [(-1, 0), (0, 1)]],
     4: [[(0, 1), (1, 0), (0, -1)],
        [(1, 0), (0, -1), (-1, 0)],
        [(0, -1), (-1, 0), (0, 1)],
        [(-1, 0), (0, 1), (1, 0)]],
     5: [[(0, 1), (1, 0), (0, -1), (-1, 0)]]
     }
idx_arr = {1: [0, 1, 2, 3], 2: [0, 1], 3: [0, 1, 2, 3], 4: [0, 1, 2, 3], 5: [0]}


def valid_range(y, x):
    if y < 0 or x < 0 or y >= n or x >= m:
        return False
    else:
        return True


def permutation():
    lv = len(vc)
    if lv == len(cctvs):
        arr_cpy = copy.deepcopy(arr)
        for idx, c in enumerate(cctvs):
            v = arr_cpy[c[0]][c[1]]
            for mov in d[v][vc[idx]]:
                sy, sx = c[0], c[1]
                while valid_range(sy, sx):
                    if arr_cpy[sy][sx] == 6:
                        break
                    elif arr_cpy[sy][sx] == 0:
                        arr_cpy[sy][sx] = '#'
                    sy, sx = sy + mov[0], sx + mov[1]
        total = 0
        for i in range(n):
            for j in range(m):
                if arr_cpy[i][j] == 0:
                    total += 1
        totals.append(total)
        return
    for elem in idx_arr[arr[cctvs[lv][0]][cctvs[lv][1]]]:
        if not visited[lv][elem]:
            visited[lv][elem] = 1
            vc.append(elem)
            permutation()
            visited[lv][elem] = 0
            vc.pop()


n, m = map(int, input().split())
arr = []
cctvs = []
cctv_n = []
for i in range(n):
    arr.append(list(map(int, input().split())))
    for j in range(m):
        if arr[i][j] >= 1 and arr[i][j] <= 5:
            cctvs.append((i, j))
            #cctv_n.append(arr[i][j])

totals = []
tst_case = []
vc = []
visited = [[0]*4 for _ in range(8)]
permutation()
print(min(totals))
