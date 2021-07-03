n = int(input())
time = []
for i in range(n):
    a, b = map(int, input().split())
    time.append([a, b])

cnt = 0
now = 0
time.sort(key=lambda x: (x[1], x[0]))

for j in range(len(time)):
    if now <= time[j][0]:
        now = time[j][1]
        cnt += 1

print(cnt)