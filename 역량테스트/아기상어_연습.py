import sys
input = sys.stdin.readline


def noFish():
    for p in range(sharkSize):
        if fishStack[p] > 0:
            return False  # 먹을 수 있는 고기 아직 있다
    return True  # 먹을 수 있는 고기 없음


def find(x, y):
    global sharkSize, eat, time, fishStack

    if noFish():
        print('nofish', time)
        exit(0)

    cant = 0
    for w in range(1, max((x, y)) * 2 + 1):
        # a = 0
        b = 0
        for a in range(w*2+1):
            if a == 0 or a == w*2:
                xx, yy = x - (w - a), y
                if xx >= 0 and yy >= 0 and xx < n and yy < n and board[xx][yy] <= sharkSize:
                    if board[xx][yy] < sharkSize and board[xx][yy] != 0:  # 먹을게 있으면
                        time += w  # 이동한 거리
                        eat += 1  # 배가 참
                        fishStack[board[xx][yy] - 1] -= 1  # 남은 물고기 최신화
                        board[xx][yy] = 9  # 상어이동
                        board[x][y] = 0  # 이전자리 0
                        if sharkSize == eat:  # 배가 다차면!!
                            eat = 0  # 레벨업
                            sharkSize += 1
                        print(board, w, sharkSize)
                        find(xx, yy)
                        return
                if a <= w:
                    b += 1
                else:
                    b -= 1
                continue
            else:
                dx = [w - a, w - a]
                dy = [-b, b]
                for d in range(2):
                    xx, yy = x - dx[d], y + dy[d]
                    if xx >= 0 and yy >= 0 and xx < n and yy < n and board[xx][yy] <= sharkSize:
                        if board[xx][yy] < sharkSize and board[xx][yy] != 0:  # 먹을게 있으면
                            time += w  # 이동한 거리
                            eat += 1  # 배가 참
                            fishStack[board[xx][yy] - 1] -= 1  # 남은 물고기 최신화
                            board[xx][yy] = 9  # 상어이동
                            board[x][y] = 0  # 이전자리 0
                            if sharkSize == eat:  # 배가 다차면!!
                                eat = 0  # 레벨업
                                sharkSize += 1
                            print(board, w, sharkSize)
                            find(xx, yy)
                            return
                if a < w:
                    b += 1
                else:
                    b -= 1
            # a += 1
    print(time, sharkSize)
    exit(0)

    # 주위에 먹을거 없음                  find(x, y, dx*c, dy*c)
    # 여기를 어떻게 해야할까!!!!!@@@@@@@@@@   (n배씩 늘리는걸 생각중, 아니면 홀수일때 dx / 짝수일때 ddx)
    # 먹을건 있지만 갈 수 없을 때!!!!는?????


fishStack = [0] * 10
sharkSize = 2
eat = 0
time = 0

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
check = [[0] * n for _ in range(n)]
'''
# up,left,right,down
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]
'''
startI, startJ = 0, 0
for i in range(n):
    for j in range(n):
        if board[i][j] == 9:
            startI, startJ = i, j
        elif board[i][j] != 0:
            fishStack[board[i][j] - 1] += 1
find(startI, startJ)
