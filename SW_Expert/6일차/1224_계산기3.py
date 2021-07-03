T = 10
for test_case in range(1, T + 1):
    length = int(input())
    table = list(map(str, input()))
    trans = []
    stack = []
    for i in range(0, length):
        if table[i] == '(':
            stack.append(table[i])
        elif table[i] == '*':
            while stack[-1] == '*':
                trans.append(stack.pop())
            stack.append(table[i])
        elif table[i] == '+':
            while stack[-1] == '*' or stack[-1] == '+':
                trans.append(stack.pop())
            stack.append(table[i])
        elif table[i] == ')':
            while stack[-1] != '(':
                trans.append(stack.pop())
            stack.pop()
        else:
            trans.append(table[i])
    while stack:
        trans.append(stack.pop())
    j = 2
    while 1:
        if len(trans) == 1:
            break
        if trans[j] == '+':
            trans[j] = int(trans[j - 2]) + int(trans[j - 1])
            del trans[j - 1]
            del trans[j - 2]
            j -= 2
        if trans[j] == '*':
            trans[j] = int(trans[j - 2]) * int(trans[j - 1])
            del trans[j - 1]
            del trans[j - 2]
            j -= 2
        j += 1
    print("#%d %d" % (test_case, trans[0]))
