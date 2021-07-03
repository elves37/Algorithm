T = 10
for test_case in range(1, T + 1):
    length = int(input())
    horizontal = [list(map(str, input())) for _ in range(8)]
    vertical = []
    count = 0
    for k in range(0, 8):
        ver = [i[k] for i in horizontal]
        vertical.append(ver)
    for a in range(0, 8):
        for b in range(0, 9-length):
            c = 0
            for d in range(0, length//2):
                if horizontal[a][b + c] == horizontal[a][b + length - 1 - c]:
                    c += 1
                    if c == (length//2):
                        count += 1
                        break
                else:
                    break
    for a in range(0, 8):
        for b in range(0, 9-length):
            c = 0
            for d in range(0, length//2):
                if vertical[a][b + c] == vertical[a][b + length - 1 - c]:
                    c += 1
                    if c == (length//2):
                        count += 1
                        break
                else:
                    break
    print("#%d %d" % (test_case, count))