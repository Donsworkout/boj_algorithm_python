import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))
d = [0] * n
d_max = [0] * n
d[0], d_max[0] = arr[0], arr[0]

for i in range(1, n):
    if d_max[i-1] < d[i-1] + arr[i]:
        d_max[i] = d[i-1] + arr[i]
    else:
        d_max[i] = d_max[i-1]
    if arr[i] > d[i-1] + arr[i]:
        d[i] = arr[i]
    else:
        d[i] = d[i-1] + arr[i]
    if d[i] > d_max[i]:
        d_max[i] = d[i]

print(d_max[n-1])

"""
최적의 해
n = int(input())
a = list(map(int, input().split()))
d = [0] * n
d[0] = a[0]
for i in range(1, n):
    d[i] = max(d[i-1] + a[i], a[i])
print(max(d))
"""