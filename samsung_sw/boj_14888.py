import itertools
import sys
input = sys.stdin.readline

n = int(input())
su_arr = list(map(int,input().split()))
a, b, c, d = map(int,input().split())
arr = []
if a > 0:
    for _ in range(a):
        arr.append('+')
if b > 0:
    for _ in range(b):
        arr.append('-')
if c > 0:
    for _ in range(c):
        arr.append('*')
if d > 0:
    for _ in range(d):
        arr.append('/')

oper_set = list(itertools.permutations(arr, len(arr)))
all_sik = []

for oper in list(set(oper_set)):
    oper = list(oper)
    sik = 0
    for i in range(len(su_arr)):
        if i == 0:
            sik = su_arr[0]
        else:
            tmp = oper.pop()
            if tmp == '+':
                sik = sik + su_arr[i]
            elif tmp == '-':
                sik = sik - su_arr[i]
            elif tmp == '*':
                sik = sik * su_arr[i]
            elif tmp == '/':
                if sik < 0:
                    sik = -((-sik) // su_arr[i])
                else:
                    sik = sik // su_arr[i]
    all_sik.append(sik)

print(max(all_sik))
print(min(all_sik))