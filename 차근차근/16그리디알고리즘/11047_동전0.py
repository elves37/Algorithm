n, k = map(int, input().split())
coin = []
cnt = 0
now = 0
for i in range(n):
    coin.append(int(input()))

while k != 0:
    now = coin.pop()
    num = 0
    if now <= k:
        num += (k // now)
        cnt += num
        k -= (num * now)

print(cnt)