import sys
input = sys.stdin.readline

dx = [-1, -1, -1, 0, 0, 1, 1, 1]    # 8방위
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

N, M, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]     # 로봇
tree = []
for i in range(N):  # 땅 초기화
    tmp = []
    for j in range(N):
        tmp.append([5])
    tree.append(tmp)

for i in range(M):      # 초기 나무
    tmp = list(map(int, input().split()))
    tree[tmp[0]-1][tmp[1]-1].append(tmp[2])     # 좌표에 나이 적용

for k in range(K):  # k년 반복
    # 봄 & 여름
    for i in range(N):
        for j in range(N):
            energy = 0
            if len(tree[i][j]) > 1:
                for t in range(len(tree[i][j])-1, 0, -1):
                    if tree[i][j][t] <= tree[i][j][0]:      # 자리 양분보다 나이가 적으면
                        tree[i][j][0] -= tree[i][j][t]      # 양분을 나이만큼 먹고
                        tree[i][j][t] += 1                  # 나이 증가
                    else:
                        energy += tree[i][j].pop(t) // 2     # 더이상 못크면 에너지가 됨
            tree[i][j][0] += energy

    # 가을
    for i in range(N):
        for j in range(N):
            for t in range(len(tree[i][j])-1, 0, -1):
                if tree[i][j][t] % 5 == 0:
                    for d in range(8):                      # 이 부분 굿!
                        x, y = i+dx[d], j+dy[d]
                        if x >= 0 and y >= 0 and x < N and y < N:
                            tree[x][y].append(1)                        # 8방위 각 맨 끝에 1살나무가 append 됨

    # 겨울
    for i in range(N):
        for j in range(N):
            tree[i][j][0] += A[i][j]        # 양분 공급

cnt = 0
for i in range(N):
    for j in range(N):
        if len(tree[i][j]) > 1:
            cnt += len(tree[i][j])-1
print(cnt)
