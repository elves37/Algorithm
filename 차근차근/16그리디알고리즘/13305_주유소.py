n = int(input())
length = list(map(int, input().split()))
oil = list(map(int, input().split()))
cost = 0

now_len = length[0]
now_oil = oil[0]
for i in range(1, n-1):
    if now_oil > oil[i]:
        cost += (now_len * now_oil)
        now_len, now_oil = length[i], oil[i]
    else:
        now_len += length[i]
cost += (now_len * now_oil)

print(cost)
