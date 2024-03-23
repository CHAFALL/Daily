'''
5 3
-1 1 2 3 4
2 2
3 4
5 6
'''


n, m = map(int, input().split())
temp = list(map(int, input().split()))
C = [[] for _ in range(n + 1)] # 상사들의 부하들 목록
ans = [0] * (n + 1)
# 뭔가 거꾸로 하면 될 것 같음..
for i in range(n-1, -1, -1):
    if temp[i] == -1:
        continue
    # 직속 상사에게 현재 직원 넣기
    C[temp[i]].append(i + 1)
    # 직속 상사에게 내(현재 직원)가 가진 부하들 다 넣기
    C[temp[i]].extend(C[i + 1])


for _ in range(m):
    idx, w = map(int, input().split())

    # 난 이미 칭찬 받았어
    ans[idx] += w

    for c in C[idx]:
        ans[c] += w

for i in range(1, n + 1):
    print(ans[i], end=' ')


