def find_load(row, col):
    global miro
    global a
    if a >= 1:
        return
    if miro[row][col+1] == 3 or miro[row+1][col] == 3 or miro[row][col-1] == 3 or miro[row-1][col] == 3:
        a += 1
        return
    if miro[row][col+1] == 1 and miro[row+1][col] == 1 and miro[row][col-1] == 1 and miro[row-1][col] == 1:
        return
    if miro[row][col+1] == 0:
        i = 1
        while miro[row][col+i] != 1:
            miro[row][col+i] = 1
            if miro[row+1][col+i] == 0 or miro[row-1][col+i] == 0:
                find_load(row, col + i)
                break
            i += 1
            if miro[row][col+i] == 3:
                a += 1
                return
    if miro[row+1][col] == 0:
        i = 1
        while miro[row + i][col] != 1:
            miro[row + i][col] = 1
            if miro[row+i][col+1] == 0 or miro[row+i][col-1] == 0:
                find_load(row + i, col)
                break
            i += 1
            if miro[row + i][col] == 3:
                a += 1
                return
    if miro[row][col-1] == 0:
        i = 1
        while miro[row][col - i] != 1:
            miro[row][col - i] = 1
            if miro[row+1][col-i] == 0 or miro[row-1][col-i] == 0:
                find_load(row, col - i)
                break
            i += 1
            if miro[row][col - i] == 3:
                a += 1
                return
    if miro[row-1][col] == 0:
        i = 1
        while miro[row - i][col] != 1:
            miro[row - i][col] = 1
            if miro[row-i][col+1] == 0 or miro[row-i][col-1] == 0:
                find_load(row - i, col)
                break
            i += 1
            if miro[row - i][col] == 3:
                a += 1
                return
    return


T = 10
for test_case in range(1, T + 1):
    int(input())
    miro = [list(map(int, input())) for _ in range(100)]
    a = 0
    find_load(1, 1)
    if a >= 1:
        print("#%d %d" % (test_case, 1))
    else:
        print("#%d %d" % (test_case, 0))
