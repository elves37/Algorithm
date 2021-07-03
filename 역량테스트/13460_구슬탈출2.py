def right(ma, red, blue, countt):
    global ans, size
    count = countt + 1
    for x in range(0, size[0]):
        for y in range(0, size[1]):
            if ma[x][-y] == 'R':
                while 1:
                    if ma[red[0]][red[1] + 1] != '#' and ma[red[0]][red[1] + 1] != 'B':
                        if ma[red[0]][red[1] + 1] == 'O':
                            ans.append(count)
                            if count == 1:
                                for ii in range(size[0]):
                                    print(ma[ii])
                            return
                        ma[red[0]][red[1]] = '.'
                        red[1] += 1
                        ma[red[0]][red[1]] = 'R'
                    else:
                        break
            elif ma[x][-y] == 'B':
                while 1:
                    if ma[blue[0]][blue[1] + 1] != '#' and ma[blue[0]][blue[1] + 1] != 'R':
                        if ma[blue[0]][blue[1] + 1] == 'O':
                            ans.append(11)
                            return
                        ma[blue[0]][blue[1]] = '.'
                        blue[1] += 1
                        ma[blue[0]][blue[1]] = 'B'
                    else:
                        break
    if count == 10:
        ans.append(11)
        return
    left(ma, red, blue, count)
    up(ma, red, blue, count)
    down(ma, red, blue, count)


def left(ma, red, blue, countt):
    global ans, size
    count = countt + 1
    for x in range(0, size[0]):
        for y in range(0, size[1]):
            if ma[x][y] == 'R':
                while 1:
                    if ma[red[0]][red[1] - 1] != '#' and ma[red[0]][red[1] - 1] != 'B':
                        if ma[red[0]][red[1] - 1] == 'O':
                            ans.append(count)
                            if count == 1:
                                for ii in range(size[0]):
                                    print(ma[ii])
                            return
                        ma[red[0]][red[1]] = '.'
                        red[1] -= 1
                        ma[red[0]][red[1]] = 'R'
                    else:
                        break
            elif ma[x][y] == 'B':
                while 1:
                    if ma[blue[0]][blue[1] - 1] != '#' and ma[blue[0]][blue[1] - 1] != 'R':
                        if ma[blue[0]][blue[1] - 1] == 'O':
                            ans.append(11)
                            return
                        ma[blue[0]][blue[1]] = '.'
                        blue[1] -= 1
                        ma[blue[0]][blue[1]] = 'B'
                    else:
                        break
    if count == 10:
        ans.append(11)
        return
    right(ma, red, blue, count)
    up(ma, red, blue, count)
    down(ma, red, blue, count)


def up(ma, red, blue, countt):
    global ans, size
    count = countt + 1
    for y in range(0, size[1]):
        for x in range(0, size[0]):
            if ma[x][y] == 'R':
                while 1:
                    if ma[red[0] - 1][red[1]] != '#' and ma[red[0] - 1][red[1]] != 'B':
                        if ma[red[0] - 1][red[1]] == 'O':
                            ans.append(count)
                            if count == 1:
                                for ii in range(size[0]):
                                    print(ma[ii])
                            return
                        ma[red[0]][red[1]] = '.'
                        red[0] -= 1
                        ma[red[0]][red[1]] = 'R'
                    else:
                        break
            elif ma[x][y] == 'B':
                while 1:
                    if ma[blue[0] - 1][blue[1]] != '#' and ma[blue[0] - 1][blue[1]] != 'R':
                        if ma[blue[0] - 1][blue[1]] == 'O':
                            ans.append(11)
                            return
                        ma[blue[0]][blue[1]] = '.'
                        blue[0] -= 1
                        ma[blue[0]][blue[1]] = 'B'
                    else:
                        break
    if count == 10:
        ans.append(11)
        return
    right(ma, red, blue, count)
    left(ma, red, blue, count)
    down(ma, red, blue, count)


def down(ma, red, blue, countt):
    global ans, size
    count = countt + 1
    for y in range(0, size[1]):
        for x in range(0, size[0]):
            if ma[-x][y] == 'R':
                while 1:
                    if ma[red[0] + 1][red[1]] != '#' and ma[red[0] + 1][red[1]] != 'B':
                        if ma[red[0] + 1][red[1]] == 'O':
                            ans.append(count)
                            if count == 1:
                                for ii in range(size[0]):
                                    print(ma[ii])
                            return
                        ma[red[0]][red[1]] = '.'
                        red[0] += 1
                        ma[red[0]][red[1]] = 'R'
                    else:
                        break
            elif ma[-x][y] == 'B':
                while 1:
                    if ma[blue[0] + 1][blue[1]] != '#' and ma[blue[0] + 1][blue[1]] != 'R':
                        if ma[blue[0] + 1][blue[1]] == 'O':
                            ans.append(11)
                            return
                        ma[blue[0]][blue[1]] = '.'
                        blue[0] += 1
                        ma[blue[0]][blue[1]] = 'B'
                    else:
                        break
    if count == 10:
        ans.append(11)
        return
    right(ma, red, blue, count)
    left(ma, red, blue, count)
    up(ma, red, blue, count)


T = 1
for test_case in range(1, T + 1):
    size = list(map(int, input().split()))
    maP = [list(map(str, input())) for _ in range(size[0])]
    ans = []
    r_loc = []
    b_loc = []
    for i in range(size[0]):
        for j in range(size[1]):
            if maP[i][j] == 'R':
                r_loc = [i, j]
            if maP[i][j] == 'B':
                b_loc = [i, j]

    check = 0

    right(maP, r_loc, b_loc, check)
    left(maP, r_loc, b_loc, check)
    up(maP, r_loc, b_loc, check)
    down(maP, r_loc, b_loc, check)

    print(ans)
    if min(ans) == 11:
        print(-1)
    else:
        print(min(ans))

'''
for i in range(size[0]):
    print(maP[i])
for ii in range(size[0]):
    print(maPP[ii])
'''