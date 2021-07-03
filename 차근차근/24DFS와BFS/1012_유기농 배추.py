import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def bug(x, y):
    visit[x][y] = False
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    for q in range(4):
        if x+dx[q] >= 0 and x+dx[q] < m and y+dy[q] >= 0 and y+dy[q] < n:
            if visit[x+dx[q]][y+dy[q]] and baechu[x+dx[q]][y+dy[q]] == 1:
                bug(x+dx[q], y+dy[q])
    return


t = int(input())
for tc in range(1, t + 1):
    m, n, k = map(int, input().split())
    baechu = [[0 for i in range(n)] for j in range(m)]
    visit = [[True for i in range(n)] for j in range(m)]
    for _ in range(k):
        a, b = map(int, input().split())
        baechu[a][b] = 1
    cnt = 0
    for i in range(m):
        for j in range(n):
            if visit[i][j] and baechu[i][j] == 1:
                cnt += 1
                bug(i, j)
    print(cnt)