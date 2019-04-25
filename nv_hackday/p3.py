def solution(T):
    len_T = len(T)
    for idx, e in enumerate(T):
        winter = T[0:idx + 1]
        summer = T[idx + 1:len_T]
        if max(winter) < min(summer):
            return len(winter)
    pass