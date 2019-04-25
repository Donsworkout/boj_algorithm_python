import sys
input = sys.stdin.readline

dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]


def valid_range(a, b):
    if a < 0 or b < 0 or a >= N or b >= N:
        return False
    else:
        return True


def feed_enough(age, pos):
    if feed[pos[0]][pos[1]] >= age:
        return True
    else:
        return False


N, M, K = map(int, input().split())
A = []
feed = [[5]*N for _ in range(N)]
m = [[[]*N for _ in range(N)] for _ in range(N)]
for _ in range(N):
    A.append(list(map(int, input().split())))
for _ in range(M):
    x, y, z = map(int, input().split())
    m[x-1][y-1].append((z, 1))

for _ in range(K):
    # 봄
    for i in range(N):
        for j in range(N):
            if not m[i][j]:
                continue
            m[i][j].sort()
            for idx, tree in enumerate(m[i][j]):
                if feed_enough(tree[0], (i, j)):
                    feed[i][j] -= tree[0]
                    m[i][j][idx] = (tree[0] + 1, 1)
                else:
                    m[i][j][idx] = (tree[0], 0)

    # 여름
    for i in range(N):
        for j in range(N):
            if not m[i][j]:
                continue
            rem = []
            for tree in m[i][j]:
                if tree[1] == 0:
                    feed[i][j] += (tree[0] // 2)
                    rem.append(tree)
            for e in rem:
                m[i][j].remove(e)

    # 가을
    for i in range(N):
        for j in range(N):
            if not m[i][j]:
                continue
            for tree in m[i][j]:
                if tree[0] % 5 == 0:
                    for d in dirs:
                        dx, dy = i + d[0], j + d[1]
                        if valid_range(dx, dy):
                            m[dx][dy].append((1, 1))

    # 겨울
    for i in range(N):
        for j in range(N):
            feed[i][j] += A[i][j]

cnt = 0
for i in range(N):
    for j in range(N):
        for tree in m[i][j]:
            if tree[1] == 1:
                cnt += 1
print(cnt)