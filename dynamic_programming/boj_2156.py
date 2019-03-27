"""
추상화가 중요합니다
연속된 조건 관련 문제같은 경우, 적용 최저점에서 테스트 해 보면서
확실하게 먹고 가는 부분은 전에 구했던 값으로 추상화 하고,
전제 조건은 현재 시점에서 판단해야 합니다
"""
import sys
input = sys.stdin.readline
d = [0] * 10000
arr = []

n = int(input())
for _ in range(n):
    arr.append(int(input()))

if n == 1:
    d[0] = arr[0]
elif n == 2:
    d[0], d[1] = arr[0], arr[0] + arr[1]
else:
    d[0], d[1], d[2] = arr[0], arr[0] + arr[1], max(arr[0] + arr[1], arr[0] + arr[2], arr[1] + arr[2])

for i in range(3, n):
    p_max = max(d[i-3] + arr[i-1] + arr[i], d[i-2] + arr[i])
    d[i] = max(p_max, d[i-1])

print(d[n-1])