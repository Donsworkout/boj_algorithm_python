import sys
input = sys.stdin.readline
method = [0] * 11


def DP(n):
    if method[n]:
        return method[n]
    else:
        method[n] = DP(n-3) + DP(n-2) + DP(n-1)
        return method[n]


method[1], method[2], method[3] = 1, 2, 4
for _ in range(int(input())):
    print(DP(int(input())))