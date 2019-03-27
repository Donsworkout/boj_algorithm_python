import sys
input = sys.stdin.readline

D = {}
for _ in range(int(input())):
    s = input()
    if s[0] in D:
        D[s[0]] += 1
    else:
        D[s[0]] = 1
p = []
for k,v in D.items():
    if v >= 5:
        p.append(k)
if p:
    print(*sorted(p),sep='')
else:
    print('PREDAJA')
