adj = {1: [2,3,4,5],
       2: [1,3,5,6],
       3: [2,3,4,6],
       4: [1,3,5,6],
       5: [1,2,4,6],
       6: [2,3,4,5]
       }

A = [1,6,2,3]

sum_arr = []
for target in A:
    sum_v = 0
    for e in A:
        if e != target:
            if target in adj[e]:
                sum_v += 1
            else:
                sum_v += 2
    sum_arr.append(sum_v)
print(min(sum_arr))