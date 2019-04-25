import sys
import math
input = sys.stdin.readline

cands = []
n, k = map(int, input().split())
arr = list(map(int, input().split()))

pk = k
while pk <= n:
    for i in range(0, n-pk+1):
        tmp = arr[i:i+pk]
        m = sum(tmp) / pk
        s = 0
        for elem in tmp:
            s += (elem - m) ** 2
        v = s / pk
        cands.append(math.sqrt(v))
    pk += 1

print(min(cands))