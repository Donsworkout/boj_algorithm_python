import collections


def valid_range(a):
    if a > 200000 or a < 0:
        return False
    else:
        return True


def bfs(c):
    cnt = 0
    c_prev = 0
    while queue:
        if c > 200000:
            return -1
        q_size = len(queue)
        for _ in range(q_size):
            cur = queue.popleft()
            print(cur,c)
            if cur >= c:
                return cnt
            if valid_range(cur-1) and not visited[cur-1]:
                queue.append(cur-1)
                visited[cur-1] = 1
            if valid_range(cur+1) and not visited[cur+1]:
                queue.append(cur+1)
                visited[cur+1] = 1
            if valid_range(cur*2) and not visited[cur*2]:
                queue.append(cur*2)
                visited[cur*2] = 1
        cnt += 1
        c_prev += 1
        c = c + c_prev
    return -1


C, B = map(int,input().split())
visited = [0]*200001
visited[B] = 1
queue = collections.deque([B])
print(bfs(C))