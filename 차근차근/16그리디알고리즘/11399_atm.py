n = int(input())
time = list(map(int, input().split()))

time.sort(reverse=True)

cnt = 0
ans = []

while time:
    cnt += time.pop()
    ans.append(cnt)

print(sum(ans))