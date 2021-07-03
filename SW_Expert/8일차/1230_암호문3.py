T = 10
for test_case in range(1, T + 1):
    length = int(input())
    secret = list(map(int, input().split()))
    num = int(input())
    command = list(map(str, input().split()))
    i = 0
    c = 0
    while 1:
        if i == len(command):
            break
        if command[i] == 'I':
            c += 1
            loc = int(command[i+1])
            count = int(command[i+2])
            for k in range(count):
                secret.insert(loc+k, int(command[i+3+k]))
        elif command[i] == 'D':
            c += 1
            loc = int(command[i + 1])
            count = int(command[i + 2])
            for k in range(count):
                del secret[loc]
        elif command[i] == 'A':
            c += 1
            count = int(command[i + 1])
            for k in range(count):
                secret.append(int(command[i+2+k]))
        if c == num:
            break
        i += 1
    print('#%d' % test_case, end=' ')
    for j in range(10):
        if j == 9:
            print('%d' % secret[j])
            break
        print('%d' % secret[j], end=' ')
