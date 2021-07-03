T = 10
for test_case in range(1, T + 1):
    dump = int(input())
    box = list(map(int, input().split()))
    dump2 = dump
    for i in range(dump):
        box[box.index(max(box))] = max(box) - 1
        box[box.index(min(box))] = min(box) + 1
        dump2 -= 1
        if(max(box) <= 1):
            break
        elif(dump == 0):
            break
    print("#%d %d" % (test_case, max(box)-min(box)))