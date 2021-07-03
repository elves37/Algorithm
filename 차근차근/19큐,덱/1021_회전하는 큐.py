import sys
from collections import deque


def second(f, t):
    q = deque(f)
    cnt = 0
    while 1:
        if q[0] == t:
            q.popleft()
            return cnt, list(q)
        q.append(q.popleft())
        cnt += 1


def third(f, t):
    q = deque(f)
    cnt = 0
    while 1:
        if q[0] == t:
            q.popleft()
            return cnt, list(q)
        q.appendleft(q.pop())
        cnt += 1


input = sys.stdin.readline
n, m = map(int, input().split())
find = list(map(int, input().split()))
answer = 0
qq = [_ for _ in range(1, n + 1)]
for i in find:
    a1, q1 = second(qq, i)
    a2, q2 = third(qq, i)
    if a1 <= a2:
        answer += a1
        qq = q1
    else:
        answer += a2
        qq = q2
print(answer)
