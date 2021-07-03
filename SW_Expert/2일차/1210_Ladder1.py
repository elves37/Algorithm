T = 10
for test_case in range(1, T + 1):
    int(input())
    ladder_map = [list(map(int, input().split())) for _ in range(100)]
    row = 98
    col = ladder_map[99].index(max(ladder_map[99]))
    while 1:
        #print(col, row)
        if col > 0 and ladder_map[row][col-1] == 1:
            while 1:
                col -= 1
                if ladder_map[row-1][col] == 1:
                    break
        elif col < 99 and ladder_map[row][col+1] == 1:
            while 1:
                col += 1
                if ladder_map[row-1][col] == 1:
                    break
        row -= 1
        if row == 0:
            break
    print("#%d %d" % (test_case, col))