T = 10
for test_case in range(1, T + 1):
    int(input())
    table = list(map(int, input().split()))
    i = 1
    while 1:
        if i == 6:
            i = 1
        if table[0]-i <= 0:
            del table[0]
            table.append(0)
            break
        else:
            table.append(table.pop(0)-i)
            i += 1
    print("#%d" % test_case, end=' ')
    for j in range(8):
        if j == 7:
            print(table[j])
            break
        print(table[j], end=' ')
