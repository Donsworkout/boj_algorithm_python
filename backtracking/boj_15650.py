import sys
input = sys.stdin.readline


def combination():
    if len(vc) == m:
        print(*vc, sep=' ')
    if vc:
        start = vc[-1]
    else:
        start = 0
    for i in range(start + 1, n+1):
        vc.append(i)
        combination()
        vc.pop()


n, m = map(int, input().split())
vc = []
combination()