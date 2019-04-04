import sys
input = sys.stdin.readline


def dfs(e, f, status):
    if not status:
        visited[e] = 1
        adj[f][e] = 1
    for elem in pt[e]:
        if not visited[elem]:
            dfs(elem, f, 0)


n = int(input())
arr = []
adj = [[0]*n for _ in range(n)]
pt = {}
for i in range(n):
    arr.append(list(map(int, input().split())))
    pt[i] = []
    for j in range(n):
        if arr[i][j] == 1:
            pt[i].append(j)

for i in range(n):
    visited = [0] * n
    dfs(i, i, 1)

for elem in adj:
    print(*elem)