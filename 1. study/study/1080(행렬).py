'''
3 4
0000
0010
0000
1001
1011
1001
'''

reverse = [1, 0]  # 0이면 1로 1이면 0으로

N, M = map(int, input().split())

arr1 = [list(map(int, input())) for _ in range(N)]
arr2 = [list(map(int, input())) for _ in range(N)]

cnt = 0
# 뒤집을 수도 없거나 처음부터 맞는 경우 걸러줌
if (N < 3 or M < 3) and arr1 != arr2:
    cnt = -1
else:
    for i in range(N - 2):
        for j in range(M - 2):
            # 현재 놈이 맞지 않다면 뒤집어!
            if arr1[i][j] != arr2[i][j]:
                cnt += 1
                for p in range(i, i + 3):
                    for q in range(j, j + 3):
                        arr1[p][q] = reverse[arr1[p][q]]

# 뒤집다가 포기한 경우
if cnt != -1:
    if arr1 != arr2:
        cnt = -1

print(cnt)

