T = int(input())
for test_case in range(1, T + 1):
    int(input())
    data = list(map(int, input().split()))
    max_data = max(data)+1
    subs = sorted(data)
    my_data = [0] * max_data
    for i in subs:
        my_data[-i] += 1
    final=101-my_data.index(max(my_data))
    print("#%d %d" % (test_case, final))