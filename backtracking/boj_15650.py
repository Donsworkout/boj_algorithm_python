import sys
input = sys.stdin.readline

def combination():
    if len(vc) == m:
        print(*vc, sep=' ')
        return
    if not vc:
        start = 1
    else:
        start = vc[-1] + 1
    for elem in range(start, n+1):
        vc.append(elem)
        combination()
        vc.pop()

n, m = map(int, input().split())
vc = []
combination()