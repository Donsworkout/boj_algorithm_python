import sys
input = sys.stdin.readline
d = [[0] * 301 for _ in range(301)]
n, m = map(int, input().split())
arr = [[0] * (m+1)]

for i in range(n):
    el = [0] + list(map(int, input().split()))
    for e, j in enumerate(el):
        d[i][j] = d[i-1][j] + d[i][j-1] - d[i-1][j-1] + e

i, j, x, y = map(int, input().split())
print(d[x][y] - d[x][j-1] - d[i-1][y] + arr[i-1][j-1])
