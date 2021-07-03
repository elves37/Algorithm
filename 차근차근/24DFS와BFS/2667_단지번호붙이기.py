import sys
input = sys.stdin.readline
n = int(input())
house = [list(map(int, list(input().strip()))) for _ in range(n)]
visit = [[True]*n for _ in range(n)]
ans = []


def dan(x, y):
    global cnt
    visit[x][y] = False
    cnt += 1
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    for i in range(4):
        if x + dx[i] < n and x + dx[i] >= 0 and y + dy[i] < n and y + dy[i] >= 0:
            if visit[x+dx[i]][y+dy[i]] and house[x+dx[i]][y+dy[i]] == 1:
                dan(x+dx[i], y+dy[i])


for k in range(n):
    for s in range(n):
        if visit[k][s] and house[k][s]:
            cnt = 0
            dan(k, s)
            ans.append(cnt)
ans.sort()
print(len(ans))
for f in ans:
    print(f)