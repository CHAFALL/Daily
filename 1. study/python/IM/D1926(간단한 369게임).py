import sys
sys.stdin = open('D1926.txt')

N = int(input())
arr = list(map(str,range(1, N+1)))
ans = []
for ar in arr:
    cnt = 0
    for a in ar:
        if a in '369':
           cnt += 1
    if cnt:
        ans.append('-' * cnt)
    else:
        ans.append(ar)

print(*ans)