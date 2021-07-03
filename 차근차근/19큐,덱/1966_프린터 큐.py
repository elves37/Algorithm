from collections import deque
t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    li = list(map(int, input().split()))
    q = deque()
    cnt = 0
    for i in li:
        q.append((i, cnt))
        cnt += 1
    ans = 0
    while q:
        q.append(q.popleft())
        if q[-1][0] == max(q)[0]:
            ans += 1
            if q.pop()[1] == m:
                print(ans)
                break
