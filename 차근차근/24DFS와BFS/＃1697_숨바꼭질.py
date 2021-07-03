from collections import deque
import sys
input = sys.stdin.readline
n, k = map(int, input().split())
if n == k:
    print(0)
else:
    cnt = 0
    visit = [True] * 100001
    q = deque()
    q.append(n)
    visit[n] = False
    while q:
        size = len(q)
        for i in range(size):
            now = q.popleft()
            if now == k:
                print(cnt)
                break
            if now-1 >= 0 and visit[now-1]:
                q.append(now-1)
                visit[now-1] = False
            if now+1 <= 100000 and visit[now+1]:
                q.append(now+1)
                visit[now+1] = False
            if now*2 <= 100000 and visit[now*2]:
                q.append(now*2)
                visit[now*2] = False
        cnt += 1