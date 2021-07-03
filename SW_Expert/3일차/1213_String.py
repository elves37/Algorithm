T = 10
for test_case in range(1, T + 1):
    int(input())
    search = str(input())
    table = list(map(str, input().split(search)))
    count = len(table) - 1
    print("#%d %d" % (test_case, count))