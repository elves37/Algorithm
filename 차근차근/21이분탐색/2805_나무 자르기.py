import sys
def main():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    tree = list(map(int, input().split()))
    tree.sort()
    start = 1
    end = tree[-1]
    answer = 0
    while end - start >= 0:
        cut = (start + end) // 2
        ans = 0
        for i in tree:
            if i - cut > 0:
                ans += (i - cut)
            if ans >= m:
                break
        if ans >= m:
            answer = max(cut, answer)
            start = cut + 1
        else:
            end = cut - 1
    print(answer)


main()