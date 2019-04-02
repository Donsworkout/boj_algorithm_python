import sys
from collections import deque
input = sys.stdin.readline


def graph_maker(a, b):
    graph[a].append(b)


def dfs(cur):
    p_v.append(cur)
    visited[cur] = 1
    for elem in sorted(graph[cur]):
        if not visited[elem]:
            dfs(elem)


def bfs():
    while queue:
        len_q = len(queue)
        for _ in range(len_q):
            cur = queue.popleft()
            for elem in sorted(graph[cur]):
                if not visited[elem]:
                    queue.append(elem)
                    p_v.append(elem)
                    visited[elem] = 1
    print(*p_v, sep=' ')


n, m, v = map(int,input().split())
graph = {}
for i in range(n):
    graph[i+1] = []
visited = [0] * (n+1)
for _ in range(m):
    a, b = map(int,input().split())
    graph_maker(a, b)
    graph_maker(b, a)

p_v = []
dfs(v)
print(*p_v, sep=' ')

visited = [0] * (n+1)
p_v = [v]
visited[v] = 1
queue = deque([v])
bfs()