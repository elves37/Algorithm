import sys
input = sys.stdin.readline
k, n = map(int, input().split())
line = []
for _ in range(k):
    line.append(int(input()))
line.sort()
start = 0
end = line[-1]
mid = line[0]
answer = 0
while end-start >= 0:
    ans = 0
    for i in line:
        ans += (i//mid)
    if ans >= n:
        answer = max(answer, mid)
        start = mid+1
    else:
        end = mid-1
    mid = (start+end)//2
print(answer)