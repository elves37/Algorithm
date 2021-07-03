T = 10
for test_case in range(1, T + 1):
    table = list(map(str, input()))
    num = []
    for i in range(3, len(table)):
        num.append(int(table[i]))
    z = 0
    while z < len(num)-1:
        if num[z] == num[z+1]:
            num.pop(z)
            num.pop(z)
            z -= 2
        z += 1
    print('#%d' % test_case, end=' ')
    for i in range(len(num)):
        if i == len(num) - 1:
            print(num[i])
            break
        print(num[i], end='')
