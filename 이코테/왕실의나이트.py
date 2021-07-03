n = input()

x, y = int(n[1]), int(ord(n[0]))-int(ord('a'))+1

step = [(-2,-1),(-2,1),(2,-1),(2,1),(-1,-2),(1,-2),(-1,2),(1,2)]

result = 0

for i in step:
    nx = x+i[0]
    ny = y+i[1]
    if nx<=8 and nx>0 and ny <=8 and ny>0:
        result += 1

print(result)
