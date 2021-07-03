def change(table, leng):
    nt = [0] * leng
    for i in range(leng):
        if table[i] == 'ZRO':
            nt[i] = 0
        elif table[i] == 'ONE':
            nt[i] = 1
        elif table[i] == 'TWO':
            nt[i] = 2
        elif table[i] == 'THR':
            nt[i] = 3
        elif table[i] == 'FOR':
            nt[i] = 4
        elif table[i] == 'FIV':
            nt[i] = 5
        elif table[i] == 'SIX':
            nt[i] = 6
        elif table[i] == 'SVN':
            nt[i] = 7
        elif table[i] == 'EGT':
            nt[i] = 8
        elif table[i] == 'NIN':
            nt[i] = 9
    return nt

def re_change(table, leng):
    nt = []
    for i in range(leng):
        if table[i] == 0:
            nt.append('ZRO')
        elif table[i] == 1:
            nt.append('ONE')
        elif table[i] == 2:
            nt.append('TWO')
        elif table[i] == 3:
            nt.append('THR')
        elif table[i] == 4:
            nt.append('FOR')
        elif table[i] == 5:
            nt.append('FIV')
        elif table[i] == 6:
            nt.append('SIX')
        elif table[i] == 7:
            nt.append('SVN')
        elif table[i] == 8:
            nt.append('EGT')
        elif table[i] == 9:
            nt.append('NIN')
    return nt


T = int(input())
for test_case in range(1, T + 1):
    inp = list(map(str, input().split()))
    length = int(inp[1])
    word = list(map(str, input().split()))
    nt = change(word, length)
    ntt = sorted(nt)
    nttt = re_change(ntt, length)
    print("#%d " % test_case)
    for k in range(length):
        if k == length - 1:
            print(nttt[k])
            break
        print(nttt[k], end=' ')