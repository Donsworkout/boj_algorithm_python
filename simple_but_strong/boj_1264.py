moeum = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
while True:
    sentence = input()
    if sentence == '#':
        break
    cnt = 0
    for letter in sentence:
        if letter in moeum:
            cnt += 1
    print(cnt)