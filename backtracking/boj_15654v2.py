#이거는 파이썬 조합 모듈 사용한 버전

from itertools import permutations
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
cases = list(permutations(arr, m))
for elem in cases:
    print(*elem, sep=' ')