height = {}
N = int(input())
for k in range(N):
    height[k] = int(input())
max_v = 0
for i in range(N):
    for j in range(i+1, N):
        if height[i] < height[j]:
            if max_v < j - i:
                max_v = j - i
            break
print(max_v)


