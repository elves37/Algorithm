def dfs(x, y, count):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return
    if miro[x][y] == 1:
        miro[x][y] = 2
        dfs(x - 1, y, count+1)
        dfs(x + 1, y, count+1)
        dfs(x, y+1, count+1)
        dfs(x, y-1, count+1)
        if x == n-1 and y == m-1:
            return result.append(count)
        return
    return


n, m = map(int, input().split())
miro = []
for i in range(n):
    miro.append(list(map(int, input())))
result = []
dfs(0, 0, 1)
print(min(result))
