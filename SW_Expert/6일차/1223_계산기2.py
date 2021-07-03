T = 10
for test_case in range(1, T + 1):
    length = int(input())
    inp = list(map(str, input()))
    for i in range(1, length-1, 2):
        if inp[i] == '*':
            inp[i], inp[i+1] = inp[i+1], inp[i]
    for i in range(1, length-1):
        if inp[i] == '+':
            inp[i], inp[i+1] = inp[i+1], inp[i]
    j = 2
    while 1:
        if len(inp) == 1:
            break
        if inp[j] == '+':
            inp[j] = int(inp[j - 2]) + int(inp[j - 1])
            del inp[j - 1]
            del inp[j - 2]
            j -= 2
        if inp[j] == '*':
            inp[j] = int(inp[j - 2]) * int(inp[j - 1])
            del inp[j - 1]
            del inp[j - 2]
            j -= 2
        j += 1
    print("#%d %d" % (test_case, inp[0]))
