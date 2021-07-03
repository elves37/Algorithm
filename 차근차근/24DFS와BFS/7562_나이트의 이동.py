from collections import deque
import sys
input = sys.stdin.readline
dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]


def move():
    q = deque()
    q.append((sx, sy))
    visit[sx][sy] = 1
    while q:
        x, y = q.popleft()
        if x == fx and y == fy:
            return visit[x][y]-1
        for i in range(8):
            newx = x+dx[i]
            newy = y+dy[i]
            if 0<=newx<l and 0<=newy<l and not(visit[newx][newy]):
                q.append((newx, newy))
                visit[newx][newy] = visit[x][y] + 1
    return -1


t = int(input())
for tc in range(1, t+1):
    l = int(input())
    sx, sy = map(int, input().split())
    fx, fy = map(int, input().split())
    if sx == fx and sy == fy:
        print(0)
    else:
        visit = [[0 for _ in range(l)] for _ in range(l)]
        print(move())