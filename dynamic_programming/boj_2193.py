import sys
input = sys.stdin.readline
method = [0] * 91


def DP(n):
    if method[n]:
        return method[n]
    else:
        method[n] = DP(n-1) + DP(n-2)
        return method[n]


method[1], method[2], method[3] = 1, 1, 2
print(DP(int(input())))