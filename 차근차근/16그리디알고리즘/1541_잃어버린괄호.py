import re
a = input()
num = list(map(int,re.findall('\d+', a)))
st = re.findall('[+-]', a)

ans = 0
plus = []
stacks = []

while st:
    now_st = st.pop()
    if now_st == '+':
        fst = num.pop()
        sst = num.pop()
        num.append(fst + sst)
    else:
        stacks.append(num.pop())

ans = num.pop()
minu = 0
while stacks:
    minu = stacks.pop()
    ans -= minu

print(ans)