cnt = 0


def dfs(arr, level, target):
    global cnt
    if level == len(arr):
        if sum(arr) == target:
            print(arr)
            cnt += 1
        else:
            return
    else:
        for i in [1, -1]:
            arr[level] *= i
            dfs(arr, level+1, target)


def solution(numbers, target):
    global cnt
    dfs(numbers, 0, target)
    return cnt


print(solution([1, 1, 1, 1, 1], 3))
