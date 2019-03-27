# 현재 과거의 관계를 잘 살필껏 (레벨 차이)
import sys
input = sys.stdin.readline
d = []
n = int(input())
for idx in range(n):
    d.append(list(map(int, input().split())))
for i in range(1, n):
    for j in range(0, i + 1):
        if j == 0:
            d[i][j] += d[i-1][j]
        elif j == i:
            d[i][j] += d[i-1][j-1]
        else:
            d[i][j] += max(d[i-1][j-1], d[i-1][j])
print(max(d[n-1]))