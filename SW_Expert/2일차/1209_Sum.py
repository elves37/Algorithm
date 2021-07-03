T = 10
for test_case in range(1, T + 1):
    int(input())
    a = [list(map(int, input().split())) for _ in range(100)]
    s = []
    bb = []
    c=[]
    d=[]
    last = []
    for k in range(0, 100):
        s.append(sum(a[k]))
        b = [i[k] for i in a]
        bb.append(sum(b))
        c.append(a[k][k])
        d.append(a[-k][-k])
    last = bb + s + c + d
    gg = max(last)
    print("#%d %d" % (test_case, gg))