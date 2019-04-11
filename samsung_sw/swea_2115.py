import sys
input = sys.stdin.readline


def get_val(pvc):
    p_sum = 0
    for p in pvc:
        p_sum += (arr[p[0]][p[1]] ** 2)
    return p_sum


def analyzer(vc, sum_v, tong):
    if len(vc) == M:
        every_case.append(get_val(vc))
        return
    for elem in tong:
        if sum_v + arr[elem[0]][elem[1]] > C:
            every_case.append(get_val(vc))
            return
        if not visited[elem[0]][elem[1]]:
            visited[elem[0]][elem[1]] = 1
            vc.append((elem[0], elem[1]))
            analyzer(vc, sum_v + arr[elem[0]][elem[1]], tong)
            vc.pop()
            visited[elem[0]][elem[1]] = 0


for cnt in range(int(input())):
    N, M, C = map(int, input().split())
    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))
    total_case = []
    for i in range(N):
        for j in range(N):
            g_visited = [[0] * N for _ in range(N)]
            if j + M > N:
                break
            else:
                tong1 = []
                for t in range(j, j + M):
                    tong1.append((i, t))
                    g_visited[i][t] = 1
                every_case = []
                visited = [[0] * N for _ in range(N)]
                analyzer([], 0, tong1)
                base_max = max(every_case)
            for k in range(i, N):
                for l in range(0, N):
                    after_max = 0
                    if l + M > N:
                        break
                    else:
                        flag = True
                        tong2 = []
                        for g in range(l, l+M):
                            if g_visited[k][g] == 0:
                                tong2.append((k, g))
                            else:
                                flag = False
                                break
                        if flag:
                            every_case = []
                            visited = [[0] * N for _ in range(N)]
                            analyzer([], 0, tong2)
                            total_case.append(base_max + max(every_case))
    print('#'+ str(cnt+1) + ' ' + str(max(total_case)))