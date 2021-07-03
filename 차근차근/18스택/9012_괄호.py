import sys
k = int(input())
for i in range(k):
    stacks = []
    a = list(map(str, sys.stdin.readline().strip()))
    for j in range(len(a)):
        b = a.pop()
        if b == ')':
            stacks.append(b)
        else:
            if stacks:
                stacks.pop()
            else:
                print('NO')
                break
        if stacks and not a:
            print("NO")
        if not a and not stacks:
            print("YES")
