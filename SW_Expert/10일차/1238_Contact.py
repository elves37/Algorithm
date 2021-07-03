# import sys
# sys.setrecursionlimit(10000)


def calling(caller):
    state = []
    global ans, table
    for k in caller:
        if table[k][0] == 0:
            table[k][0] = 1
            for j in range(1, len(table[k])):
                if table[table[k][j]][0] == 0:
                    state.append(table[k][j])
    if not state:
        ans = caller
    else:
        calling(state)


T = 10
for test_case in range(1, T + 1):
    init = list(map(int, input().split()))
    length = init[0]
    start = init[1]
    before_table = list(map(int, input().split()))
    table = [[0] for _ in range(101)]
    for i in range(0, length - 1, 2):
        table[before_table[i]].append(before_table[i + 1])
    for i in range(0, len(table)):
        table[i] = list(set(table[i]))
    start_state = []
    table[start][0] = 1
    for i in range(1, len(table[start])):
        start_state.append(table[start][i])
    ans = []
    calling(start_state)
    print('#%d %d' % (test_case, max(ans)))
