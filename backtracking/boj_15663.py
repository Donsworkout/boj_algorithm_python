import sys
input = sys.stdin.readline


def permutation():
    global cases
    if len(vc) == m and tuple(vc):
        cases.add(tuple(vc))
    for idx, elem in enumerate(candidates):
        if not visited[elem][idx]:
            visited[elem][idx] = 1
            vc.append(elem)
            permutation()
            vc.pop()
            visited[elem][idx] = 0


n, m = map(int, input().split())
candidates = sorted(list(map(int, input().split())))
visited = [[0] * 8 for _ in range(10001)]
vc = []
cases = set()
permutation()

for case in sorted(list(cases)):
    print(*case, sep=' ')