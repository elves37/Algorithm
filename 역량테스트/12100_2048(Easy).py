from sys import stdin
from collections import deque
from copy import deepcopy


def move(de, dir, board):
  global N
  if dir == 0:  # 좌->우
    for i in range(N):  # 한 줄
      q = deque()
      for e in range(N):
        q.append(board[i][e])
      ans = deque()
      stack = list()
      zero = 0
      for k in range(N):  # 한 칸
        check1 = q.pop()
        if check1 == 0:
          zero += 1
        elif not stack:
          stack.append(check1)
        else:
          check2 = stack.pop()
          if check1 == check2:
            zero += 1
            ans.appendleft((check1*2))
          else:
            stack.append(check1)
            ans.appendleft(check2)
      while stack:
        ans.appendleft(stack.pop())
      for z in range(zero):
        ans.appendleft(0)
      for w in range(N):
        board[i][w] = ans.popleft()

  if dir == 1:  # 좌<-우
    for i in range(N):
      q = deque()
      for e in range(N):
        q.append(board[i][e])
      ans = deque()
      stack = list()
      zero = 0
      for k in range(N):  # 한 줄씩 이동
        check1 = q.popleft()
        if check1 == 0:
          zero += 1
        elif stack:
          check2 = stack.pop()
          if check1 == check2:
            zero += 1
            ans.append(check1*2)
          else:
            stack.append(check1)
            ans.append(check2)
        else:
          stack.append(check1)
      while stack:
        ans.append(stack.pop())
      for z in range(zero):
        ans.append(0)
      for w in range(N):
        board[i][w] = ans.pop()

  if dir == 2:  # 상<-하
    for i in range(N):
      q = deque()
      for e in range(N):
        q.append(board[e][i])
      ans = deque()
      stack = list()
      zero = 0
      for k in range(N):  # 한 줄씩 이동
        check1 = q.popleft()
        if check1 == 0:
          zero += 1
        elif stack:
          check2 = stack.pop()
          if check1 == check2:
            zero += 1
            ans.append(check1*2)
          else:
            stack.append(check1)
            ans.append(check2)
        else:
          stack.append(check1)
      while stack:
        ans.append(stack.pop())
      for z in range(zero):
        ans.append(0)
      for w in range(N):
        board[w][i] = ans.popleft()

  if dir == 3:  # 상->하
    for i in range(N):
      q = deque()
      for e in range(N):
        q.append(board[e][i])
      ans = deque()
      stack = list()
      zero = 0
      for k in range(N):  # 한 줄씩 이동
        check1 = q.pop()
        if check1 == 0:
          zero += 1
        elif stack:
          check2 = stack.pop()
          if check1 == check2:
            zero += 1
            ans.appendleft(check1*2)
          else:
            stack.append(check1)
            ans.appendleft(check2)
        else:
          stack.append(check1)
      while stack:
        ans.appendleft(stack.pop())
      for z in range(zero):
        ans.appendleft(0)
      for w in range(N):
        board[w][i] = ans.popleft()
  find(de+1, board)


def find(depth, board11):
  global pr, N
  score = 0
  if depth == 5:
    for n in range(N):
      for m in range(N):
        score = max(score, board11[n][m])
    pr = max(pr, score)
    return
  for d in range(4):
    move(depth, d, deepcopy(board11))


N = int(stdin.readline())
board1 = [list(map(int, stdin.readline().split())) for _ in range(N)]

pr = 0

find(0, deepcopy(board1))
print(pr)
