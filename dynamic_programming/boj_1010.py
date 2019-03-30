import sys
input = sys.stdin.readline

for _ in range(int(input())):
    N, M = map(int,input().split())
    if N == M:
        print(1)
        continue
    if N > (M // 2):
        cha = M - N
    else:
        cha = N
    i, j, b_1, b_2 = M, cha, 1, 1
    while i > M - cha:
        b_1 = b_1 * i
        i -= 1
    while j > 0:
        b_2 = b_2 * j
        j -= 1
    print(b_1 // b_2)