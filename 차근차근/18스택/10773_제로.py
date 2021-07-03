import sys
k = int(input())
stacks = []
for i in range(k):
    a = int(sys.stdin.readline())
    if a == 0:
        stacks.pop()
    else:
        stacks.append(a)
print(sum(stacks))
