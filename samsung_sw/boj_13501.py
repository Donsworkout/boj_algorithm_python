import collections
def bfs():
    max_v = 0
    while queue:
        q_size = len(queue)
        for _ in range(q_size):
            cur = queue.popleft()
            idx,past_sum = cur[0],cur[1]
            adder = table[idx][0]
            if idx + adder < n:
                k = adder
                while idx + k < n:
                    if (idx + k, past_sum + table[idx][1]) not in visited:
                        new_sum = past_sum + table[idx][1]
                        queue.append((idx + k, new_sum))
                        visited.append((idx + k, new_sum))
                        if max_v < new_sum:
                            max_v = new_sum
                    k += 1
            elif idx + adder == n:
                new_sum = past_sum + table[idx][1]
                if max_v < new_sum:
                    max_v = new_sum
    print(max_v)

n = int(input())
table = []
visited = []
queue = collections.deque([])
for i in range(n):
    table.append(list(map(int,input().split())))
    queue.append((i, 0))
bfs()