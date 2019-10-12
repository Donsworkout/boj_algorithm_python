def solution(skill, skill_trees):

    # 스킬 의존성 해시 세팅
    dep = {}
    for idx in range(1, len(skill)):
        dep[skill[idx]] = skill[idx-1]

    # 의존성 문제 없는 스킬트리 카운터
    cnt = 0

    # 스킬트리 순회하며 의존성 체크
    for skill_tree in skill_trees:
        status = True
        for idx, elem in enumerate(skill_tree):
            if elem in dep and (dep[elem] not in skill_tree[0:idx]):
                status = False
                break
        if status:
            cnt += 1

    return cnt


print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))