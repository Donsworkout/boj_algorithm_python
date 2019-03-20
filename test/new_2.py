alps = []
nums = []
fake_eq = input().strip()
idx = 0
while idx < len(fake_eq):
    s = fake_eq[idx]
    if s.isdigit():
        if idx < len(fake_eq) - 1 and s == '1' and fake_eq[idx + 1] == '0':
            nums.append(s + fake_eq[idx + 1])
            idx += 2
            continue
        else:
            nums.append(s)
    else:
        if s.isupper():
            alps.append(s)
        else:
            alps[-1] += s
    idx += 1
if len(alps) != len(nums):
    print('error')
else:
    chemical_eq = ''
    for i in range(len(alps)):
        chemical_eq += alps[i]
        if nums[i] != '1':
            chemical_eq += nums[i]
    print(chemical_eq)