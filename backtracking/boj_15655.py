import sys
input = sys.stdin.readline


def combination():
    if len(vc) == m:
        for idx in vc:
            print(candidates[idx], end=' ')
        print('')
    if vc:
        start = vc[-1] + 1
    else:
        start = 0
    for i in range(start, n):
        vc.append(i)
        combination()
        vc.pop()


n, m = map(int, input().split())
candidates = sorted(list(map(int, input().split())))
vc = []
combination()