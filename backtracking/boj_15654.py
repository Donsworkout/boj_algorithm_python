import sys
input = sys.stdin.readline


def permutation():
    if len(vc) == m:
        print(*vc, sep=' ')
        return
    for elem in candidates:
        if not visited[elem]:
            visited[elem] = 1
            vc.append(elem)
            permutation()
            vc.pop()
            visited[elem] = 0


n, m = map(int, input().split())
candidates = sorted(list(map(int, input().split())))
visited = [0] * 10001
vc = []
permutation()