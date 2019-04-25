def combinations(vc):
    if len(vc) == N:
        all_comb.append(list(vc))
        return
    if len(vc) != 0:
        min_idx = arr.index(vc[-1])
    else:
        min_idx = -1
    for idx, elem in enumerate(arr):
        if idx > min_idx:
            vc.append(elem)
            combinations(vc)
            vc.pop()
    return all_comb


arr = sorted(list(input().split()))
N = int(input())
all_comb = []
combinations([])
print(all_comb)