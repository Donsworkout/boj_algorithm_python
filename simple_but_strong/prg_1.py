def solution(scoville, K):
    cnt = 0
    sorted_scvs = sorted(scoville, reverse=True)

    while (True):
        sorted_scvs = sorted(sorted_scvs, reverse=True)
        if sorted_scvs[-1] >= K:
            return cnt
        elif len(sorted_scvs) == 1:
            return -1
        else:
            mixed_scv = sorted_scvs[-1] + 2 * sorted_scvs[-2]
            del sorted_scvs[-1]
            del sorted_scvs[-1]
            sorted_scvs.append(mixed_scv)
            cnt += 1

print(solution([1, 2, 3, 9, 10, 12], 7))