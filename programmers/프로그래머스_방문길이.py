def is_valid(tup):
    if tup[0] > 5 or tup[1] > 5 or tup[0] < -5 or tup[1] < -5:
        return False
    else:
        return True


def move(d):
    if d == 'U':
        return 0, 1
    elif d == 'D':
        return 0, -1
    elif d == 'R':
        return 1, 0
    else:
        return -1, 0


def solution(dirs):
    pos = 0, 0
    visited = []
    for d in dirs:
        org_pos = pos
        tmp_pos = pos[0] + move(d)[0], pos[1] + move(d)[1]
        if is_valid(tmp_pos):
            pos = tmp_pos
            if {org_pos, tmp_pos} not in visited:
                visited.append({org_pos, pos})
    return len(visited)

print(solution("LULLLLLLU"))