first = list(map(int, input().split()))
size = [first[0], first[1]]
dice_loc = [first[2], first[3]]
order_num = first[4]
table = [list(map(int, input().split())) for _ in range(size[0])]
order = list(map(int, input().split()))
dice_hor = [0, 0, 0]
dice_ver = [0, 0, 0, 0]
for i in range(order_num):
    if order[i] == 1:
        if dice_loc[1] + 1 > size[1] - 1:
            continue
        else:
            dice_loc[1] += 1
            dice_hor.append(dice_ver.pop())
            dice_ver.append(dice_hor.pop(0))
            dice_ver[1] = dice_hor[1]
            if table[dice_loc[0]][dice_loc[1]] == 0:
                table[dice_loc[0]][dice_loc[1]] = dice_hor[1]
            else:
                dice_hor[1] = table[dice_loc[0]][dice_loc[1]]
                dice_ver[1] = dice_hor[1]
                table[dice_loc[0]][dice_loc[1]] = 0
            print(dice_ver[3])
    elif order[i] == 2:
        if dice_loc[1] - 1 < 0:
            continue
        else:
            dice_loc[1] -= 1
            dice_hor.insert(0, dice_ver.pop())
            dice_ver.append(dice_hor.pop())
            dice_ver[1] = dice_hor[1]
            if table[dice_loc[0]][dice_loc[1]] == 0:
                table[dice_loc[0]][dice_loc[1]] = dice_hor[1]
            else:
                dice_hor[1] = table[dice_loc[0]][dice_loc[1]]
                dice_ver[1] = dice_hor[1]
                table[dice_loc[0]][dice_loc[1]] = 0
            print(dice_ver[3])
    elif order[i] == 3:
        if dice_loc[0] - 1 < 0:
            continue
        else:
            dice_loc[0] -= 1
            dice_ver.insert(0, dice_ver.pop())
            dice_hor[1] = dice_ver[1]
            if table[dice_loc[0]][dice_loc[1]] == 0:
                table[dice_loc[0]][dice_loc[1]] = dice_ver[1]
            else:
                dice_ver[1] = table[dice_loc[0]][dice_loc[1]]
                dice_hor[1] = dice_ver[1]
                table[dice_loc[0]][dice_loc[1]] = 0
            print(dice_ver[3])
    elif order[i] == 4:
        if dice_loc[0] + 1 > size[0] - 1:
            continue
        else:
            dice_loc[0] += 1
            dice_ver.append(dice_ver.pop(0))
            dice_hor[1] = dice_ver[1]
            if table[dice_loc[0]][dice_loc[1]] == 0:
                table[dice_loc[0]][dice_loc[1]] = dice_ver[1]
            else:
                dice_ver[1] = table[dice_loc[0]][dice_loc[1]]
                dice_hor[1] = dice_ver[1]
                table[dice_loc[0]][dice_loc[1]] = 0
            print(dice_ver[3])