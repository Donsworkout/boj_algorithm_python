# 전체를 다시 탐색해도 상관 없음 어차피 n^2
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
d = [0]*n
for i in range(0, n):
    if i == 0:
        d[i] = 1
    else:
        m = 0
        for j in range(i):
            if (arr[j] < arr[i]) and (m < d[j]):
                m = d[j]
        d[i] = m + 1
print(max(d))