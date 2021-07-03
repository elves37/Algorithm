T = 10
for test_case in range(1, T + 1):
    length = int(input())
    inp = list(map(str, input()))
    for i in range(1, length-1):
        if inp[i] == '+':
            inp[i] = inp[i+1]
            inp[i+1] = '+'
    for j in range(length):
        if j >= 2:
            if inp[j] == '+':
               inp[j] = int(inp[j-2]) + int(inp[j-1])
    print("#%d %d" % (test_case, inp[length-1]))
