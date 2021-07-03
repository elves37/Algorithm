import sys
input = sys.stdin.readline
n = int(input())
k = int(input())
left = 1
right = k
answer = 0
while left <= right:
    cnt = 0
    mid = (left+right)//2
    for i in range(1, n+1):
        cnt += min(mid//i, n)
    if cnt >= k:
        right = mid-1
        answer = mid
    else:
        left = mid+1
print(answer)