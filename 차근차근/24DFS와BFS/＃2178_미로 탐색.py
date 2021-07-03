import sys
from collections import deque
input = sys.stdin.readline
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def find(i, j):
    visit[i][j] = False
    check[i][j] = 1
    que = deque()
    que.append((i, j))
    while que:
        x, y = que.popleft()
        for k in range(4):
            newx = x+dx[k]
            newy = y+dy[k]
            if newx >= 0 and newx < n and newy >= 0 and newy < m:
                if miro[newx][newy] != 0 and visit[newx][newy]:
                    check[newx][newy] = check[x][y]+1
                    visit[newx][newy] = False
                    que.append((newx, newy))


n, m = map(int, input().split())
miro = [list(map(int, list(input().strip()))) for _ in range(n)]
visit = [[True]*m for _ in range(n)]
check = [[0]*m for _ in range(n)]
find(0, 0)
print(check[n-1][m-1])
