import sys
n = int(input())
sol = []
cnt = 0
pm = []
dt = 1
for i in range(n):
    num = int(sys.stdin.readline())
    while cnt < num:
        cnt += 1
        sol.append(cnt)
        pm.append('+')
    if sol[-1] == num:
        sol.pop()
        pm.append('-')
    else:
        dt = 0
        break

if dt == 0:
    print('NO')
else:
    for k in pm:
        print(k)
