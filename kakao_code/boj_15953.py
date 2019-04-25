festa_2017 = [0] + [5000000] * 1 + [3000000] * 2 + [2000000] * 3 + [500000] * 4 + [300000] * 5 + [100000] * 6
festa_2018 = [0] + [5120000] * 1 + [2560000] * 2 + [1280000] * 4 + [640000] * 8 + [320000] * 16
res = []

for _ in range(int(input())):
    a, b = map(int, input().split())
    r_2017 = a <= 21 and festa_2017[a] or 0
    r_2018 = b <= 31 and festa_2018[b] or 0
    res.append(r_2017 + r_2018)
print(*res, sep ='\n')