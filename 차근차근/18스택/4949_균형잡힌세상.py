import sys
while True:
    stacks = []
    dt = 1
    a = sys.stdin.readline().rstrip()
    if a[0] == '.':
        break
    for i in a:
        if i == '(' or i == '[':
            stacks.append(i)
        elif i == ')':
            if stacks and stacks[-1] == '(':
                stacks.pop()
            else:
                dt = 0
                break
        elif i == ']':
            if stacks and stacks[-1] == '[':
                stacks.pop()
            else:
                dt = 0
                break
    if dt and not(stacks):
        print('yes')
    else:
        print('no')
