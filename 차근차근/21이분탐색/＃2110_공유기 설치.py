import sys
input = sys.stdin.readline
n, c = map(int, input().split())
x = [int(input()) for _ in range(n)]
x.sort()
left = 1
right = x[-1]-x[0]
step = 0
answer = 0
while right >= left:
    start = x[0]
    mid = (right+left)//2
    cnt = 1
    for i in range(n):
        step = x[i] - start
        if mid <= step:
            cnt += 1
            start = x[i]
    if cnt >= c:
        answer = mid
        left = mid+1
    else:
        right = mid-1
print(answer)