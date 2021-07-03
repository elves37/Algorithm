import sys
input = sys.stdin.readline


def vir(i):
    global ans
    ans += 1
    visit[i] = False
    for j in range(1, len(link[i])):
        if visit[link[i][j]]:
            vir(link[i][j])
    return


pc = int(input())
n = int(input())
link = [[0] for _ in range(pc+1)]
for i in range(n):
    a, b = map(int, input().split())
    link[a].append(b)
    link[b].append(a)
visit = [True for _ in range(pc+1)]
ans = 0
vir(1)
print(ans-1)