T = 10
for test_case in range(1, T + 1):
    length = int(input())
    table = list(map(str, input()))
    i = 0
    final = 0
    while 1:
        if not table:
            final = 1
            break
        if i >= len(table):
            break
        if table[i] == ')' or table[i] == ']' or table[i] == '}' or table[i] == '>':
            if i == 0:
                break
            if ')' in table[i]:
                if table[i - 1] == '(':
                    del table[i]
                    del table[i - 1]
                    i = 0
                    continue
                else:
                    break
            if ']' in table[i]:
                if table[i - 1] == '[':
                    del table[i]
                    del table[i - 1]
                    i = 0
                    continue
                else:
                    break
            if '}' in table[i]:
                if table[i - 1] == '{':
                    del table[i]
                    del table[i - 1]
                    i = 0
                    continue
                else:
                    break
            if '>' in table[i]:
                if table[i - 1] == '<':
                    del table[i]
                    del table[i - 1]
                    i = 0
                    continue
                else:
                    break
        i += 1
    print("#%d %d" % (test_case, final))