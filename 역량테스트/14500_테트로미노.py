def nemo(mapping):
    plus = list()
    for i in range(0, size[0] - 1):
        for j in range(0, size[1] - 1):
            plus.append(mapping[i][j] + mapping[i][j + 1] + mapping[i + 1][j] + mapping[i + 1][j + 1])
    return max(plus)


def stick(mapping):
    plus = list()
    for i in range(0, size[0]):
        for j in range(0, size[1] - 3):
            plus.append(mapping[i][j] + mapping[i][j + 1] + mapping[i][j + 2] + mapping[i][j + 3])
    for i in range(0, size[0] - 3):
        for j in range(0, size[1]):
            plus.append(mapping[i][j] + mapping[i + 1][j] + mapping[i + 2][j] + mapping[i + 3][j])
    return max(plus)


def giyeok(mapping):
    plus = list()
    for i in range(0, size[0] - 2):
        for j in range(0, size[1] - 1):
            plus.append(mapping[i][j] + mapping[i + 1][j] + mapping[i + 2][j] + mapping[i + 2][j + 1])
    for i in range(1, size[0]):
        for j in range(0, size[1] - 2):
            plus.append(mapping[i][j] + mapping[i][j + 1] + mapping[i][j + 2] + mapping[i - 1][j + 2])
    for i in range(0, size[0] - 2):
        for j in range(0, size[1] - 1):
            plus.append(mapping[i][j] + mapping[i][j + 1] + mapping[i + 1][j + 1] + mapping[i + 2][j + 1])
    for i in range(0, size[0] - 1):
        for j in range(0, size[1] - 2):
            plus.append(mapping[i][j] + mapping[i][j + 1] + mapping[i + 1][j] + mapping[i][j + 2])
    for i in range(2, size[0]):
        for j in range(0, size[1] - 1):
            plus.append(mapping[i][j] + mapping[i][j + 1] + mapping[i - 1][j + 1] + mapping[i - 2][j + 1])
    for i in range(0, size[0] - 1):
        for j in range(0, size[1] - 2):
            plus.append(mapping[i][j] + mapping[i][j + 1] + mapping[i][j + 2] + mapping[i + 1][j + 2])
    for i in range(0, size[0] - 2):
        for j in range(0, size[1] - 1):
            plus.append(mapping[i][j] + mapping[i][j + 1] + mapping[i + 1][j] + mapping[i + 2][j])
    for i in range(0, size[0] - 1):
        for j in range(0, size[1] - 2):
            plus.append(mapping[i][j] + mapping[i + 1][j] + mapping[i + 1][j + 1] + mapping[i + 1][j + 2])
    return max(plus)


def geadan(mapping):
    plus = list()
    for i in range(0, size[0] - 2):
        for j in range(0, size[1] - 1):
            plus.append(mapping[i][j] + mapping[i + 1][j] + mapping[i + 1][j + 1] + mapping[i + 2][j + 1])
    for i in range(1, size[0] - 1):
        for j in range(0, size[1] - 2):
            plus.append(mapping[i][j] + mapping[i][j + 1] + mapping[i - 1][j + 1] + mapping[i - 1][j + 2])
    for i in range(1, size[0] - 1):
        for j in range(0, size[1] - 1):
            plus.append(mapping[i][j] + mapping[i + 1][j] + mapping[i][j + 1] + mapping[i - 1][j + 1])
    for i in range(0, size[0] - 1):
        for j in range(0, size[1] - 2):
            plus.append(mapping[i][j] + mapping[i][j + 1] + mapping[i + 1][j + 1] + mapping[i + 1][j + 2])
    return max(plus)


def oh(mapping):
    plus = list()
    for i in range(0, size[0] - 1):
        for j in range(0, size[1] - 2):
            plus.append(mapping[i][j] + mapping[i][j + 1] + mapping[i][j + 2] + mapping[i + 1][j + 1])
    for i in range(1, size[0] - 2):
        for j in range(0, size[1] - 1):
            plus.append(mapping[i][j] + mapping[i][j + 1] + mapping[i - 1][j + 1] + mapping[i + 1][j + 1])
    for i in range(1, size[0]):
        for j in range(0, size[1] - 2):
            plus.append(mapping[i][j] + mapping[i][j + 1] + mapping[i][j + 2] + mapping[i - 1][j + 1])
    for i in range(0, size[0] - 2):
        for j in range(0, size[1] - 1):
            plus.append(mapping[i][j] + mapping[i + 1][j] + mapping[i + 2][j] + mapping[i + 1][j + 1])
    return max(plus)


size = list(map(int, input().split()))
table = [list(map(int, input().split())) for _ in range(size[0])]
ans = list()
ans.append(nemo(table))
ans.append(stick(table))
ans.append(giyeok(table))
ans.append(geadan(table))
ans.append(oh(table))
print(max(ans))