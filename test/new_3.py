table1 = {}
table2 = {}
table3 = {}
header1 = {}
header2 = {}
header3 = {}
key1 = []
key2 = []

n1 = int(input())
header1 = list(input().split())
for idx in range(n1-1):
    row = list(input().split())
    key_v = int(row[0])
    key1.append(key_v)
    del row[0]
    table1[key_v] = row

n2 = int(input())
header2 = list(input().split())
for idx in range(n2-1):
    row = list(input().split())
    key_v = int(row[0])
    key2.append(key_v)
    del row[0]
    table2[key_v] = row

header2.remove('id')
header3 = header1 + header2

for idx in key1:
    if idx in table2:
        table3[idx] = table1[idx] + table2[idx]
    else:
        table3[idx] = table1[idx] + ['NULL'] * len(header2)

print(*header3)
for y in sorted(table3):
    L = str(table3[y])
    a = ''.join(L).replace('[', '').replace(']', '').replace(',', '').replace("'", '')
    print(y, a)
