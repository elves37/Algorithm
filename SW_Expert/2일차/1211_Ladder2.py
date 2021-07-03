T = 10
for test_case in range(1, T + 1):
    int(input())
    ladder_map = [list(map(int, input().split())) for _ in range(100)]
    count_arr = []
    for i in range(100):
        row = 1
        col = i
        count = 0
        if ladder_map[0][i] == 1:
            while 1:
                if col > 0 and ladder_map[row][col - 1] == 1:
                    while 1:
                        col -= 1
                        count += 1
                        if ladder_map[row + 1][col] == 1:
                            break
                elif col < 99 and ladder_map[row][col + 1] == 1:
                    while 1:
                        col += 1
                        count += 1
                        if ladder_map[row + 1][col] == 1:
                            break
                row += 1
                count += 1
                if row == 99:
                    count_arr.append(count)
                    break
        elif ladder_map[0][i] == 0:
            count_arr.append(1000)
    best = count_arr.index(min(count_arr))
    print("#%d %d" % (test_case, best))