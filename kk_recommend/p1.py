# Enter your code here. Read input from STDIN. Print output to STDOUT
win_against = {'R': 'P', 'P': 'S', 'S': 'R'}


def win(pst, tmp_arr):
    if tmp_arr[pst] == win_against[tmp_arr[pst + 1]]:
        return True
    else:
        return False


def handFormationChange(arr, poi_pos, cnt):
    global change_cnt
    if len(arr) == 1:
        print(change_cnt)
        return True
    new_arr = []
    # 길이 짝수일때
    if len(arr) % 2 == 0:
        pos = 0
        iter_cnt = 0
        while pos <= len(arr) - 2:
            if pos == poi_pos:
                new_arr.append(win_against[arr[pos + 1]])
                if cnt != 0 and arr[poi_pos] != win_against[arr[pos + 1]]:
                    change_cnt += 1
                poi_pos = iter_cnt
            elif pos + 1 == poi_pos:
                new_arr.append(win_against[arr[pos]])
                if cnt != 0 and arr[poi_pos] != win_against[arr[pos]]:
                    change_cnt += 1
                poi_pos = iter_cnt
            else:
                if arr[pos] == arr[pos + 1]:
                    pos += 2
                    continue
                if win(pos, arr):
                    new_arr.append(arr[pos])
                else:
                    new_arr.append(arr[pos + 1])
            pos += 2
            iter_cnt += 1
    # 길이 홀수일때
    else:
        pos = 0
        iter_cnt = 0
        while pos <= len(arr) - 1:
            if pos == len(arr) - 1 and poi_pos != pos:
                new_arr.append(arr[pos])
                break
            elif pos == len(arr) - 1 and poi_pos == pos:
                poi_pos = iter_cnt
                new_arr.append(arr[pos])
                cnt = -1
                break
            if pos == poi_pos:
                new_arr.append(win_against[arr[pos + 1]])
                if cnt != 0 and arr[poi_pos] != win_against[arr[pos + 1]]:
                    change_cnt += 1
                poi_pos = iter_cnt
            elif pos + 1 == poi_pos:
                new_arr.append(win_against[arr[pos]])
                if cnt != 0 and arr[poi_pos] != win_against[arr[pos]]:
                    change_cnt += 1
                poi_pos = iter_cnt
            else:
                if arr[pos] == arr[pos + 1]:
                    pos += 2
                    continue
                if win(pos, arr):
                    new_arr.append(arr[pos])
                else:
                    new_arr.append(arr[pos + 1])
            pos += 2
            iter_cnt += 1
    handFormationChange(new_arr, poi_pos, cnt+1)


n = int(input())
poi = int(input())
st_arr = list(input())
st_arr.insert(poi, 0)
change_cnt = 0
handFormationChange(st_arr, poi, 0)
