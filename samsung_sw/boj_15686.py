import sys
from itertools import combinations

input = sys.stdin.readline

n, m = map(int, input().split())
arr = []
houses = []
chickens = []
for i in range(n):
    arr.append(list(map(int, input().split())))
    for j in range(n):
        if arr[i][j] == 1:
            houses.append((i, j))
        elif arr[i][j] == 2:
            chickens.append((i, j))

c_idx = [i for i in range(len(chickens))]
all_cases = list(combinations(c_idx, m))
sums = []
for elem in all_cases:
    d_sum = 0
    for h in houses:
        dst_arr = []
        for e in list(elem):
            c = chickens[e]
            dst_arr.append(abs(h[0] - c[0]) + abs(h[1] - c[1]))
        d_sum += min(dst_arr)
    sums.append(d_sum)
print(min(sums))