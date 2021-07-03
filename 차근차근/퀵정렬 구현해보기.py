import time
import random


def q_sort(target):
    if len(target) <= 1:
        return target
    pivot = target[len(target)//2]
    lower, equal, upper = [], [], []
    for i in target:
        if i < pivot:
            lower.append(i)
        elif i > pivot:
            upper.append(i)
        else:
            equal.append(i)
    return q_sort(lower) + equal + q_sort(upper)


ls = [x for x in range(10001)] # 10000개의 원소를 갖는 리스트
random.shuffle(ls) # 정렬하기 전 무작위로 섞기
ls2 = ls[:] # 퀵 정렬에 사용할 리스트

start_time = time.time()
q_sort(ls)
print(time.time()-start_time)

start_time = time.time()
ls.sort()
print(time.time()-start_time)
