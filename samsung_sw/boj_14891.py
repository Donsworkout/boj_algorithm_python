from collections import deque
import copy
left = {2: 1, 3: 2, 4: 3}
right = {1: 2, 2: 3, 3: 4}


def move(n, d):
    if len(chk) == 4:
        return
    original = copy.deepcopy(T)
    if d == 1:
        T[n].rotate(1)
    else:
        T[n].rotate(-1)
    chk.append(n)
    if n in left and left[n] not in chk:
        if original[n][-2] != original[left[n]][2]:
            move(left[n], -d)
    if n in right and right[n] not in chk:
        if original[n][2] != original[right[n]][-2]:
            move(right[n], -d)

T = [deque([0])*8 for _ in range(5)]
for i in range(1, 5):
    inp = input()
    for j in range(8):
        T[i][j] = int(inp[j])

rep = int(input())
for _ in range(rep):
    chk = []
    a, b = map(int, input().split())
    move(a, b)

score = 0
if T[1][0] == 1:
    score += 1
if T[2][0] == 1:
    score += 2
if T[3][0] == 1:
    score += 4
if T[4][0] == 1:
    score += 8
print(score)