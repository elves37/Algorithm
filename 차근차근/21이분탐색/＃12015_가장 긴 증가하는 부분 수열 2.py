import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
ans = [0]
for i in a:
    if ans[-1] < i:
        ans.append(i)
    else:
        left = 0
        right = len(ans)-1
        while left < right:
            mid = (left+right)//2
            if ans[mid] >= i:
                right = mid
            else:
                left = mid+1
        ans[right] = i
print(len(ans)-1)