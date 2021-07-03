room = int(input())
a = list(map(int, input().split()))
bc = list(map(int, input().split()))
b = bc[0]
c = bc[1]
count = 0
for i in range(room):
    bm = a[i] - b
    if bm >= 0:
        count += 1
        if bm % c == 0:
            count += (bm // c)
        else:
            count += ((bm // c) + 1)
    else:
        count += 1
print(count)
