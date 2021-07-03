T = 10

for test_case in range(1, T + 1):
    total = 0
    count = int(input())
    buildings = list(map(int, input().split()))
    for i in range(2, count - 2):
        subs = sorted(buildings[i - 2:i + 3])
        current = buildings[i]
        second = subs[3]
        visible = current - second
        if visible > 0:
            total += visible
    print("#%d %d" % (test_case, total))