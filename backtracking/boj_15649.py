import sys
input = sys.stdin.readline


def permutation():
    if len(vc) == m:
        print(*vc, sep=' ')
    for i in range(1, n+1):
        if not visited[i]:
            visited[i] = 1
            vc.append(i)
            permutation()
            vc.pop()
            visited[i] = 0


n, m = map(int, input().split())
visited = [0] * 9
vc = []
cases = []
permutation()