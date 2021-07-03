T = 10
for test_case in range(1, T + 1):
    int(input())
    horizontal = [list(map(str, input())) for _ in range(100)]
    vertical = []
    table = []
    for k in range(0, 100):
        ver = [i[k] for i in horizontal]
        vertical.append(ver)
    for a in range(0, 100):
        length = 2
        for length in range(2, 101):
            count = 0
            for b in range(0, 101 - length):
                c = 0
                for d in range(0, length // 2):
                    if horizontal[a][b + c] == horizontal[a][b + length - 1 - c]:
                        c += 1
                        if c == (length // 2):
                            count += 1
                            break
                    else:
                        break
                if count == 1:
                    table.append(length)
                    break
    for a in range(0, 100):
        length = 2
        for length in range(2, 101):
            count = 0
            for b in range(0, 101 - length):
                c = 0
                for d in range(0, length // 2):
                    if vertical[a][b + c] == vertical[a][b + length - 1 - c]:
                        c += 1
                        if c == (length // 2):
                            count += 1
                            break
                    else:
                        break
                if count == 1:
                    table.append(length)
                    break
    MAX = max(table)
    print("#%d %d" % (test_case, MAX))