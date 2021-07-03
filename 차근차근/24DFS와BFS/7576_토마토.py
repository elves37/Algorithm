import sys
from collections import deque
input = sys.stdin.readline
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def yum(x, y):
    visit[x][y] = 0
    for k in range(4):
        newx = x+dx[k]
        newy = y+dy[k]
        if newx >= 0 and newx < n and newy >= 0 and newy < m and box[newx][newy] == 0 and visit[newx][newy] == 1:
            box[newx][newy] = 1
            to.append((newx, newy))


m, n = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(n)]
visit = [[1]*m for _ in range(n)]
now = []
to = []
for q in range(n):
    for w in range(m):
        if box[q][w] == 1:
            now.append((q, w))
        elif box[q][w] == -1:
            visit[q][w] = 0
day = -1
while now:
    a, b = now.pop()
    yum(a, b)
    if not(now):
        now = to
        to = []
        day += 1
if sum(sum(h) for h in visit) > 0:
    print(-1)
else:
    print(day)