import sys
input = sys.stdin.readline

n = int(input())
d = [[0]*10 for _ in range(1001)]
d[1] = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
for i in range(2,n+1):
    for j in range(0,10):
        if j == 0:
            d[i][j] = d[i-1][j]
        else:
            for k in range(0, j+1):
                d[i][j] += d[i-1][k]
print(sum(d[n]) % 10007)