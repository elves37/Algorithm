def find_load(miro_map, row, col):
    in_miro = miro_map
    if in_miro[row][col+1] == 3 or in_miro[row+1][col] == 3 or in_miro[row][col-1] == 3 or in_miro[row-1][col] == 3:
        global a
        a += 1
        return
    if in_miro[row][col+1] == 1 and in_miro[row+1][col] == 1 and in_miro[row][col-1] == 1 and in_miro[row-1][col] == 1:
        return
    if in_miro[row][col+1] == 0:
        in_miro[row][col] = 1
        find_load(in_miro, row, col+1)
    if in_miro[row+1][col] == 0:
        in_miro[row][col] = 1
        find_load(in_miro, row+1, col)
    if in_miro[row][col-1] == 0:
        in_miro[row][col] = 1
        find_load(in_miro, row, col-1)
    if in_miro[row-1][col] == 0:
        in_miro[row][col] = 1
        find_load(in_miro, row-1, col)
    return


T = 10
for test_case in range(1, T + 1):
    int(input())
    miro = [list(map(int, input())) for _ in range(16)]
    a = 0
    find_load(miro, 1, 1)
    if a >= 1:
        print("#%d %d" % (test_case, 1))
    else:
        print("#%d %d" % (test_case, 0))
