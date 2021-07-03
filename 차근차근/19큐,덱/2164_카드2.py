from collections import deque

n = int(input())
pack = deque([i for i in range(1, n+1)])
while len(pack) != 1:
    pack.popleft()
    pack.append(pack.popleft())
print(pack[0])
