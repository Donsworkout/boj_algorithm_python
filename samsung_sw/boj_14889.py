import itertools
import sys
input = sys.stdin.readline

n = int(input())
arr = []
members = []
results = []


def combination_by_don(mbs, s):
    reversed_arr = set()
    vc = []

    def comb():
        if len(vc) == s:
            converted = tuple([mbs[e] for e in vc])
            if converted not in reversed_arr:
                converted_r = tuple(sorted(list(set(members) - set(converted))))
                add_cases = itertools.permutations(list(converted), 2)
                team1 = 0
                for add_case in add_cases:
                    team1 += arr[add_case[0]][add_case[1]]

                add_cases_r = itertools.permutations(list(converted_r), 2)
                team2 = 0
                for add_case_r in add_cases_r:
                    team2 += arr[add_case_r[0]][add_case_r[1]]

                reversed_arr.add(converted_r)
                results.append(abs(team1 - team2))
                return

        start = vc[-1] + 1 if vc else 0
        for k in range(start, n):
            vc.append(k)
            comb()
            vc.pop()
    comb()


for _ in range(n):
    arr.append(list(map(int, input().split())))

for i in range(n):
    members.append(i)

combination_by_don(members, n//2)

print(min(results))