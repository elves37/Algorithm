#표 몇칸씩 이동하면서 삭제 하고 돌려놓고

def solution(n, k, cmd):
    answer = ''

    temp_list = [i for i in range(n)]
    pop_list = []


    for order in cmd:

        # print('{}를 실행합니다.'.format(order))
        if order[0] == 'D':
            if k + int(order[2:]) >= len(temp_list):
                k = len(temp_list) - 1
            else:
                k += int(order[2:])
        elif order[0] == 'C':
            pop_list.append([temp_list[k], k])
            if k == len(temp_list) - 1:
                k -= 1
                temp_list.pop()
            else:
                temp_list.pop(k)
        elif order[0] == 'U':
            if k - int(order[2:]) <= 0:
                k = 0
            else:
                k -= int(order[2:])
        elif order[0] == 'Z':
            temp_list.insert(pop_list[-1][1], pop_list[-1][0])
            if pop_list[-1][1] <= k:
                k += 1
            pop_list.pop()
        # print('현재 인덱스는 {}이고 그 값은 {}입니다.'.format(k, temp_list[k]))
        # print(temp_list)
        # print(pop_list)

    for i in range(n):
        if i in temp_list:
            answer += 'O'
        else:
            answer += 'X'

    return answer