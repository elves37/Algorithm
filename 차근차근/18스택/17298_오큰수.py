import sys
N = int(input())
num = list(map(int, sys.stdin.readline().split()))
stacks = [0]
sol = [-1] * N
cnt = 1

while stacks and cnt < N:
    while stacks and num[stacks[-1]] < num[cnt]:
        sol[stacks[-1]] = num[cnt]
        stacks.pop()
    stacks.append(cnt)
    cnt += 1

for i in sol:
    print(i, end=' ')