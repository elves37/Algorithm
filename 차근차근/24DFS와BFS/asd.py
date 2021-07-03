answer = []
visit = []
def can(x,y,move,places):
    global answer, visit
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    visit[x][y] = False
    if move == 2:
        return
    for i, j in zip(dx, dy):
        if x+i >= 0 and y+j >= 0 and x+i<5 and y+j<5 and places[x+i][y+j] != 'X' and visit[x+i][y+j]:
            if places[x+i][y+j] == 'P':
                #print(x+i,y+j,move)
                answer.append(1)
                return
            can(x+i,y+j,move+1,places)
    return

def solution(places):
    global answer, visit
    ans = []
    for q in range(len(places)):
        for w in range(5):
            for e in range(5):
                if places[q][w][e] == 'P':
                    visit = [[True] * 5 for _ in range(5)]
                    #print('visit')
                    can(w,e,0,places[q])
        if sum(answer) == 0:
            ans.append(1)
        else:
            ans.append(0)
        answer = []
    return ans


print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))