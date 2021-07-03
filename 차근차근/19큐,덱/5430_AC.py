import sys
from collections import deque
import re
input = sys.stdin.readline
t = int(input())
for tc in range(1, t+1):
    p = list(input())
    n = int(input())
    q = deque(list(map(int, re.findall("\d+", input()))))
    er = True
    dire = True
    for i in p:
        if i == 'R':
            dire = not(dire)
        elif i == 'D':
            if q:
                if dire:
                    q.popleft()
                else:
                    q.pop()
            else:
                print('error')
                er = False
                break
    if er:
        if dire:
            print(str(list(q)).replace(" ", ""))
        else:
            q.reverse()
            print(str(list(q)).replace(" ", ""))
