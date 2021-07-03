import sys
input = sys.stdin.readline
n = list(map(int, input().split()))
size = n[0]
tree_num = n[1]
year = n[2]
S2D2 = [list(map(int, input().split())) for _ in range(size)]
tree = [list(map(int, input().split())) for _ in range(tree_num)]
check = []
for i in range(tree_num):
    check.append([tree[i][0]-1, tree[i][1]-1])
ground = [[[5]*1000 for _ in range(size)] for _ in range(size)]
for i in range(tree_num):
    for s in range(tree[i][2]):
        if s == tree[i][2] - 1:
            ground[tree[i][0] - 1][tree[i][1] - 1].append(1)
        else:
            ground[tree[i][0] - 1][tree[i][1] - 1].append(0)


def spring():
    for q in check:
        peed = 0
        a = check.pop()
        i, j = a[0], a[1]
        for k in range(1000):
            while ground[i][j][k] > 0:
                if ground[i][j][0] - k > 0:
                    ground[i][j][0] -= k
                    ground[i][j][k] -= 1
                else:  # 여름
                    peed += (k // 2) * ground[i][j][k]
                    ground[i][j][k] = 0
        ground[i][j][0] += peed
        if sum(ground[i][j]) == ground[i][j][0]:
            check.pop(a)
        else:
            check.append(a)


def fall():
    for a in check:
        i, j = a[0], a[1]
        for k in range(1000):
            if ground[i][j][k] % 5 == 0:
                if i - 1 >= 0:
                    if j - 1 >= 0:
                        if len(ground[i - 1][j - 1]) == 1:
                            ground[i - 1][j - 1].append(1)
                        else:
                            ground[i - 1][j - 1][1] += 1
                        if [i - 1, j - 1] not in check:
                            check.append([i - 1, j - 1])
                    if len(ground[i - 1][j]) == 1:
                        ground[i - 1][j].append(1)
                    else:
                        ground[i - 1][j][1] += 1
                    if [i - 1, j] not in check:
                        check.append([i - 1, j])
                    if j + 1 < size:
                        if len(ground[i - 1][j + 1]) == 1:
                            ground[i - 1][j + 1].append(1)
                        else:
                            ground[i - 1][j + 1][1] += 1
                        if [i - 1, j + 1] not in check:
                            check.append([i - 1, j + 1])
                if j - 1 >= 0:
                    if len(ground[i][j - 1]) == 1:
                        ground[i][j - 1].append(1)
                    else:
                        ground[i][j - 1][1] += 1
                    if [i, j - 1] not in check:
                        check.append([i, j - 1])
                if j + 1 < size:
                    if len(ground[i][j + 1]) == 1:
                        ground[i][j + 1].append(1)
                    else:
                        ground[i][j + 1][1] += 1
                    if [i, j + 1] not in check:
                        check.append([i, j + 1])
                if i + 1 < size:
                    if j - 1 >= 0:
                        if len(ground[i + 1][j - 1]) == 1:
                            ground[i + 1][j - 1].append(1)
                        else:
                            ground[i + 1][j - 1][1] += 1
                        if [i + 1, j - 1] not in check:
                            check.append([i + 1, j - 1])
                    if len(ground[i + 1][j]) == 1:
                        ground[i + 1][j].append(1)
                    else:
                        ground[i + 1][j][1] += 1
                    if [i + 1, j] not in check:
                        check.append([i + 1, j])
                    if j + 1 < size:
                        if len(ground[i + 1][j + 1]) == 1:
                            ground[i + 1][j + 1].append(1)
                        else:
                            ground[i + 1][j + 1][1] += 1
                        if [i + 1, j + 1] not in check:
                            check.append([i + 1, j + 1])


def winter():
    for i in range(size):
        for j in range(size):
            ground[i][j][0] += S2D2[i][j]


while year > 0:
    spring()
    fall()
    winter()
    year -= 1
sum_ = 0
for i in range(size):
    for j in range(size):
        sum_ = sum(ground[i][j][0:])
print(sum_)
