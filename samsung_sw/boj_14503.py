import sys
input = sys.stdin.readline

dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
l_d = {0: 3, 1: 0, 2: 1, 3: 2}
arr = []


def valid_range(a, b):
    if a < 0 or b < 0 or a >= n or b >= m:
        return False
    else:
        return True


def clean(y, x, cd):
    global cnt
    arr[y][x] = '#'
    cnt += 1
    while True:
        alive = False
        for mov in dirs:
            if valid_range(y + mov[0], x + mov[1]) and (arr[y + mov[0]][x + mov[1]] == 0):
                alive = True
                break
        if not alive:
            if not valid_range(y + dirs[cd-2][0], x + dirs[cd-2][1]) or (arr[y + dirs[cd-2][0]][x + dirs[cd-2][1]] == 1):
                print(cnt)
                sys.exit()
            elif valid_range(y + dirs[cd-2][0], x + dirs[cd-2][1]) and (arr[y + dirs[cd-2][0]][x + dirs[cd-2][1]] != 1):
                y, x = y + dirs[cd-2][0], x + dirs[cd-2][1]
                continue
        else:
            l_move = dirs[l_d[cd]]
            if valid_range(y + l_move[0], x + l_move[1]) and (arr[y + l_move[0]][x + l_move[1]] == 0):
                clean(y + l_move[0], x + l_move[1], l_d[cd])
            else:
                cd = l_d[cd]
                continue


n, m = map(int, input().split())
r, c, d = map(int, input().split())
for _ in range(n):
    arr.append(list(map(int, input().split())))
cnt = 0
clean(r, c, d)