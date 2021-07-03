N = int(input())
step = input().split()

x, y = 1, 1
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
dir = ['L', 'R', 'U', 'D']

for i in step:
    for a in range(4):
        if i == dir[a]:
            nx = x + dx[a]
            ny = y + dy[a]
    if nx < 1 or nx > N or ny < 1 or ny > N:
        continue

    x, y = nx, ny

print(x, y)
