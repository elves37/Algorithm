from collections import deque
import sys
input = sys.stdin.readline
dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]





k = int(input())
for tc in range(1, k+1):
    v, e = map(int, input().split())
    for i in range(e):
