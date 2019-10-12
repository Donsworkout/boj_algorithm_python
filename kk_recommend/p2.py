from itertools import combinations

numberOfAttributes = int(input())
supportThreshold = float(input())
numberOfRows = int(input())
table = []
for _ in range(numberOfRows):
    table.append(input().split(','))

all_cases = []
for row in table:
    all_cases += list(combinations(row, numberOfAttributes))
for case in set(all_cases):
    cnt = 0
    for row in table:
        if set(case) <= set(row):
            cnt += 1
    if supportThreshold <= cnt / numberOfRows:
        print(str(case).replace(" ","").replace("'","").replace(")","").replace("(",""))

#for a in answer:
#   print(str(a).replace("'","").replace(")","").replace("(",""))