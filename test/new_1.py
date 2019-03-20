import math
n = 16
w = int(math.sqrt(n))
while n % w != 0:
    w += 1
print(abs(w-(n//w)))