T = 10
for test_case in range(1, T + 1):
    int(input())
    data = list(map(int, input().split()))
    nn = data[1] - 1
    ver = 1
    def squared(num, n):
        global ver
        ver *= num
        n -= 1
        if n != 0:
            squared(num, n)
    squared(data[0], data[1])
    print("#%d %d" % (test_case, ver))