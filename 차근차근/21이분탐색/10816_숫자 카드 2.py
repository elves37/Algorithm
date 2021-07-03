import sys
input = sys.stdin.readline
n = int(input())
card1 = {}
for i in list(map(int, input().split())):
    try: card1[i] += 1
    except: card1[i] = 1
m = int(input())
card2 = list(map(int, input().split()))
for i in card2:
    try: print(card1[i], end=' ')
    except: print(0, end=' ')