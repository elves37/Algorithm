from collections import deque
import sys
input = sys.stdin.readline
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def find():
    q = deque()
    q.append((0, 0, 0))
    visit[0][0][0] = 1
    while q:
        x, y, boom = q.popleft()
        if x == n - 1 and y == m - 1:
            return visit[n-1][m-1][boom]
        for _ in range(4):
            newx = x + dx[_]
            newy = y + dy[_]
            if 0 <= newx < n and 0 <= newy < m and not(visit[newx][newy][boom]):
                if ap[newx][newy] == 0:
                    q.append((newx, newy, boom))
                    visit[newx][newy][boom] = visit[x][y][boom] + 1
                if ap[newx][newy] == 1 and boom == 0:
                    q.append((newx, newy, 1))
                    visit[newx][newy][1] = visit[x][y][boom] + 1
    return -1


n, m = map(int, input().split())
ap = [list(map(int, list(input().strip()))) for _ in range(n)]
visit = [[[0, 0] for _ in range(m)] for _ in range(n)]
print(find())