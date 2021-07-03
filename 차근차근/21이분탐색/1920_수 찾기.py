import sys
input = sys.stdin.readline
n = int(input())
nl = list(map(int, input().split()))
nl.sort()
m = int(input())
ml = list(map(int, input().split()))
for i in ml:
    start = 0
    end = len(nl)-1
    mid = int((end+start)/2)
    answer = 0
    while end-start >= 0:
        mid = int((end + start) / 2)
        if nl[mid] == i:
            answer = 1
            break
        elif nl[mid] < i:
            start = mid+1
        elif nl[mid] > i:
            end = mid-1
    print(answer)