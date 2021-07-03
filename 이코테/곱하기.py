N = input()

first = int(N[0])

for i in range(1,len(N)):
    num = int(N[i])
    if num <= 1 or first <= 1:
        first += num
    else:
        first *= num

print(first)
