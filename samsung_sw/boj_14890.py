import sys
input = sys.stdin.readline

arr = []
N, L = map(int, input().split())
built = [[0]*N for _ in range(N)]
for _ in range(N):
    arr.append(list(map(int, input().split())))

cnt = 0
for fixed in range(N):
    state = True
    for cur in range(N):
        if cur != 0:
            if arr[fixed][cur] > arr[fixed][cur-1]:
                if cur - L >= 0 and abs(arr[fixed][cur] - arr[fixed][cur-1]) == 1:
                    for pos in range(cur-L, cur):
                        if built[fixed][pos] or (not built[fixed][pos] and arr[fixed][pos] != arr[fixed][cur] - 1):
                            state = False
                            break
                    if state:
                        for k in range(cur-L, cur):
                            built[fixed][k] = 1
                else:
                    state = False
                    break
            elif arr[fixed][cur] < arr[fixed][cur-1]:
                if cur + L <= N and abs(arr[fixed][cur] - arr[fixed][cur-1]) == 1:
                    for pos in range(cur, cur+L):
                        if built[fixed][pos] or (not built[fixed][pos] and arr[fixed][pos] != arr[fixed][cur-1] - 1):
                            state = False
                            break
                    if state:
                        for k in range(cur, cur+L):
                            built[fixed][k] = 1
                else:
                    state = False
                    break
    if state:
        cnt += 1

built = [[0]*N for _ in range(N)]

for fixed in range(N):
    state = True
    for cur in range(N):
        if cur != 0:
            if arr[cur][fixed] > arr[cur-1][fixed]:
                if cur - L >= 0 and abs(arr[cur][fixed] - arr[cur-1][fixed]) == 1:
                    for pos in range(cur - L, cur):
                        if built[pos][fixed] or (not built[pos][fixed] and arr[pos][fixed] != arr[cur][fixed] - 1):
                            state = False
                            break
                    if state:
                        for k in range(cur - L, cur):
                            built[k][fixed] = 1
                else:
                    state = False
                    break
            elif arr[cur][fixed] < arr[cur-1][fixed]:
                if cur + L <= N and abs(arr[cur][fixed] - arr[cur-1][fixed]) == 1:
                    for pos in range(cur, cur+L):
                        if built[pos][fixed] or (not built[pos][fixed] and arr[pos][fixed] != arr[cur-1][fixed] - 1):
                            state = False
                            break
                    if state:
                        for k in range(cur, cur+L):
                            built[k][fixed] = 1
                else:
                    state = False
                    break
    if state:
        cnt += 1

print(cnt)