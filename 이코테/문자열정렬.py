n = input()
result = []
value = 0

for i in n:
    if i.isalpha():
        result.append(i)
    else:
        value += int(i)

result.sort()

if value != 0:
    result.append(str(value))

print(''.join(result))
