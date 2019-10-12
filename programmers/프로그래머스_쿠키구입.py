sum_table = [[0]*2001 for i in range(2001)]


def dp_sum(a, b, cookie):
    if a == b:
        return cookie[a]
    else:
        if sum_table[a][b] != 0:
            return sum_table[a][b]
        else:
            sum_table[a][b] = dp_sum(a, b - 1, cookie) + cookie[b]
            return sum_table[a][b]


def solution(cookie):
    c_len = len(cookie)
    max_val = 0

    for i in range(0, c_len-1):
        for j in range(i+2, c_len+1):
            for m in range(i+1, j):
                prev = dp_sum(i, m-1, cookie)
                post = dp_sum(m, j-1, cookie)
                if prev > post:
                    break
                if prev == post and max_val < prev:
                    max_val = prev

    return max_val

#ar = [1,1,2,3,3]
#print(dp_sum(1, 4, ar))
print(solution([1,1,2,3]))