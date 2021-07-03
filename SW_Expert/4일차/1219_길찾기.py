def fun(i):
    if first[i] != 100:
        current = first[i]
        if current == 99:
            global count
            count = 1
            return count
        fun(current)
    if second[i] != 100:
        current = second[i]
        if current == 99:
            #global count
            count = 1
            return count
        fun(current)
T = 10
for test_case in range(1, T + 1):
    length = list(map(int, input().split()))
    table = list(map(int, input().split()))
    first = [100] * 100
    second = [100] * 100
    count = 0
    a = 0
    while 1:
        first[table[a*2]] = table[a*2+1]
        a += 1
        if a < 0 or a >= length[1]:
            break
        second[table[a * 2]] = table[a * 2 + 1]
        a += 1
        if a < 0 or a >= length[1]:
            break
    fun(0)
    print("#%d %d" % (test_case, count))

