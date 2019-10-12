"""
lst = list(map(int, s.split()))
"""

import sys
input = sys.stdin.readline


arr = [0 for _ in range(501)]


def factorial(n):
    if n <= 1:
        return 1
    elif arr[n] != 0:
        return arr[n]
    else:
        arr[n] = n * factorial(n-1)
        return arr[n]


val = int(input())
res = str(factorial(val))

cnt = 0
for num in reversed(res):
    if num == "0":
        cnt += 1
    else:
        break

print(cnt)
