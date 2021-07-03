from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
q = deque()
for _ in range(n):
    command = input().split()
    if 'push' in command[0]:
        if 'front' in command[0]:
            q.appendleft(command[1])
        else:
            q.append(command[1])
    elif 'pop' in command[0]:
        if 'front' in command[0]:
            if q:
                print(q.popleft())
            else:
                print(-1)
        else:
            if q:
                print(q.pop())
            else:
                print(-1)
    elif command[0] == 'size':
        print(len(q))
    elif command[0] == 'empty':
        if q:
            print(0)
        else:
            print(1)
    elif command[0] == 'front':
        if q:
            print(q[0])
        else:
            print(-1)
    elif command[0] == 'back':
        if q:
            print(q[-1])
        else:
            print(-1)
