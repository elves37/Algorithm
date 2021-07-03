T = 10
for test_case in range(1, T + 1):
    int(input())
    table = [list(map(int, input().split())) for _ in range(100)]
    t_table = [[table[y][x] for y in range(100)]for x in range(100)]
    count = 0
    k = 0
    while 1:
        if k == 100:
            break
        j = 0
        while 1:
            if j == 100:
                break
            if t_table[k][j] == 2:
                if j == 0:
                    t_table[k][j] = 0
                else:
                    jj = j
                    while 1:
                        jj -= 1
                        if jj < 0:
                            break
                        if t_table[k][jj] == 2:
                            if jj == j - 1:
                                break
                            else:
                                t_table[k][jj + 1] = 2
                                t_table[k][j] = 0
                                break
                        if t_table[k][jj] == 1:
                            t_table[k][j] = 0
                            t_table[k][j - ((j - jj - 1) // 2)] = 2
                            t_table[k][jj] = 0
                            t_table[k][jj + ((j - jj - 1) // 2)] = 1
                            break
            j += 1
        k += 1
    w = 0
    while 1:
        if w == 100:
            break
        d = 0
        while 1:
            if d == 100:
                break
            if t_table[w][d] == 1:
                if d == 99:
                    t_table[w][d] = 0
                else:
                    if d < 98:
                        if t_table[w][d + 1] == 2 or t_table[w][d + 2] == 2:
                            count += 1
                            d += 1
                    elif d == 98:
                        if t_table[w][d + 1] == 2:
                            count += 1
                            d += 1
            d += 1
        w += 1
    print("#%d %d" % (test_case, count))