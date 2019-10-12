import collections
import sys

input = sys.stdin.readline


def bfs():
    global cnt, queue
    while queue:
        for _ in range(len(queue)):
            cur = queue.popleft()
            if visited[cur]:
                cnt += 1
                continue
            else:
                visited[cur] = 1
            for elem in arr[cur]:
                queue.append(elem)
    return cnt


n, m = map(int, input().split())
arr = [[] for _ in range(n + 1)]
visited = [0 for _ in range(n + 1)]
queue = collections.deque([])
cnt = 0

for _ in range(m):
    s, e = map(int, input().split())
    arr[s].append(e)

for i in range(1, n+1):
    queue.append(i)
#print(queue)
print(bfs())
