def time_converter(t_list):
    for idx, e in enumerate(t_list):
        if e[0] == '0':
            t_list[idx] = t_list[idx][1]
    return int(t_list[0]), int(t_list[1]), int(t_list[2])


a_list = list(input().split(':'))
b_list = list(input().split(':'))

h1, m1, s1 = time_converter(a_list)
h2, m2, s2 = time_converter(b_list)

sv1 = (3600 * h1) + (60 * m1) + s1
sv2 = (3600 * h2) + (60 * m2) + s2
sv = sv2 - sv1

nh = sv // 3600
nm = (sv - (nh * 3600)) // 60
ns = sv - (nh * 3600) - ((sv - (nh * 3600)) // 60) * 60

if nh < 0:
    nh = 24 + nh
result = [str(nh), str(nm), str(ns)]

for idx, e in enumerate(result):
    if len(e) == 1:
        result[idx] = '0' + e
print(result[0] + ":" + result[1] + ":" + result[2])