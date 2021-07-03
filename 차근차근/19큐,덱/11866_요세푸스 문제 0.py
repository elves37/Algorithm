from collections import deque

n, k = map(int, input().split())
q = deque([i for i in range(1, n+1)])
cnt = 0
answer = []
while q:
    cnt += 1
    if cnt == k:
        answer.append(q.popleft())
        cnt = 0
    else:
        q.append(q.popleft())
print('<' + str(answer)[1:-1] + '>')
