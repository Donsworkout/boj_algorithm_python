import itertools
import sys
input = sys.stdin.readline

n = int(input())
arr = []
members = []
results = []

for _ in range(n):
    arr.append(list(map(int, input().split())))

for i in range(n):
    members.append(i)

all_cases = list(itertools.combinations(members, n//2))

for case in all_cases:
    add_cases = itertools.permutations(case, 2)
    team1 = 0
    for add_case in add_cases:
        team1 += arr[add_case[0]][add_case[1]]

    left_case = tuple(set(members) - set(case))
    left_add_cases = itertools.permutations(left_case, 2)
    team2 = 0
    for left_add_case in left_add_cases:
        team2 += arr[left_add_case[0]][left_add_case[1]]
    results.append(abs(team1 - team2))
print(min(results))