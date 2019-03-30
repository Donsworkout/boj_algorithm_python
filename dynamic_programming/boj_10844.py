import sys
input = sys.stdin.readline

d = [[0] * 10 for _ in range(101)]
d[1] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]

n = int(input())
for i in range(2, n+1):
    for j in range(0, 10):
        if j == 0:
            d[i][j] = d[i-1][j+1]
        elif j == 9:
            d[i][j] = d[i-1][j-1]
        else:
            d[i][j] = d[i-1][j-1] + d[i-1][j+1]
print(sum(d[n]) % 1000000000)
