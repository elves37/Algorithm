T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    a = list(map(int, input().split()))
    profit = 0
    while a:
        profit += (max(a) * (a.index(max(a)))) - sum(a[0:a.index(max(a))])
        del a[0:a.index(max(a))+1]
    print("#%d %d" % (test_case, profit))