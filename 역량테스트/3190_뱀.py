def move(inp):
    global head_col, head_row
    if inp == 0:
        head_col -= 1
    elif inp == 1:
        head_row += 1
    elif inp == 2:
        head_col += 1
    elif inp == 3:
        head_row -= 1


def move_tail(inp):
    global tail_col, tail_row
    if inp == 0:
        tail_col -= 1
    elif inp == 1:
        tail_row += 1
    elif inp == 2:
        tail_col += 1
    elif inp == 3:
        tail_row -= 1


size = int(input())
mAP = list(([0] * size) for _ in range(size))
apple = int(input())
location = [list(map(int, input().split())) for _ in range(apple)]
for i in range(len(location)):
    mAP[location[i][0]-1][location[i][1]-1] = 2
change = int(input())
direction = [list(map(str, input().split())) for _ in range(change)]
h_time, t_time = 0, 0
head_col, head_row = 0, 0
tail_col, tail_row = 0, 0
mAP[0][0] = 1
h_go, t_go = 1, 1
h_tic, t_tic = 0, 0
while 1:
    move(h_go)
    if head_col > size-1 or head_row > size-1 or head_col < 0 or head_row < 0 or mAP[head_col][head_row] == 1:
        print(h_time+1)
        break
    if mAP[head_col][head_row] == 0:
        mAP[tail_col][tail_row] = 0
        move_tail(t_go)
    elif mAP[head_col][head_row] == 2:
        t_time -= 1
    mAP[head_col][head_row] = 1
    h_time += 1
    t_time += 1
    if h_tic < change and h_time == int(direction[h_tic][0]):
        if direction[h_tic][1] == 'L':
            h_go = (h_go+3) % 4
        elif direction[h_tic][1] == 'D':
            h_go = (h_go+1) % 4
        h_tic += 1
    if t_tic < change and t_time == int(direction[t_tic][0]):
        if direction[t_tic][1] == 'L':
            t_go = (t_go+3) % 4
        elif direction[t_tic][1] == 'D':
            t_go = (t_go+1) % 4
        t_tic += 1
'''for i in range(size):
    print(mAP[i])
'''
