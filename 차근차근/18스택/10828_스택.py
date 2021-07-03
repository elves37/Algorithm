from collections import deque
import sys

n = int(input())
stacks = deque()
for i in range(n):
    a = list(map(str, sys.stdin.readline().split()))
    if a[0] == 'push':
        stacks.append(int(a[1]))
    elif a[0] == 'pop':
        if stacks:
            print(stacks.pop())
        else:
            print(-1)
    elif a[0] == 'size':
        print(len(stacks))
    elif a[0] == 'empty':
        if stacks:
            print(0)
        else:
            print(1)
    elif a[0] == 'top':
        if stacks:
            b = stacks.pop()
            stacks.append(b)
            print(b)
        else:
            print(-1)
