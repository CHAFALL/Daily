import sys
sys.stdin = open('D1221.txt')



T = int(input())
check_list = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
for _ in range(1, T+1):
    tc, N = input().split()
    text = input().split()

    ans = ''
    for i in range(10):
        for tx in text:
            if tx == check_list[i]:
                ans += check_list[i]+' '

    print(tc)
    print(ans)


