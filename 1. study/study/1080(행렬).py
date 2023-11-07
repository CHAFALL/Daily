'''
3 4
0000
0010
0000
1001
1011
1001
'''


# reverse = [1, 0]
#
# # 만약에 불가능한 것이 있으면 -1을 출력.
# N, M = map(int, input().split())
#
# arr1 = [list(map(int, input())) for _ in range(N)]
# arr2 = [list(map(int, input())) for _ in range(N)]
#
# cnt = 0
# if N < 3 or M < 3:
#     cnt = -1
# else:
#     for i in range(N - 2):
#         for j in range(M - 2):
#             if arr1 != arr2:
#                 cnt += 1
#                 for p in range(i, i+3):
#                     for q in range(j, j+3):
#                         arr1[p][q] = reverse[arr1[p][q]]
#
# print(cnt)
#


# 같은 곳은 두번 이상 뒤집는 것은 의미 없으니깐
# 뒤집을지 말지만 판단 해주면 될 듯.
# 뒤집을 때마다 카운트,
# 뒤집는 것 구현.




n, m = map(int, input().split())
listA = []
for _ in range(n): # 리스트A 선언
    listA.append(list(map(int, list(input()))))
listB = []
for _ in range(n): # 리스트B 선언
    listB.append(list(map(int, list(input()))))


def check(i, j): # 뒤집기 함수
    for x in range(i, i+3):
        for y in range(j, j+3):
            if listA[x][y] == 0:
                listA[x][y] = 1
            else:
                listA[x][y] = 0


cnt = 0 # 카운트
if (n < 3 or m < 3) and listA != listB:
    # 예외 1, 리스트가 작을 때
    cnt = -1
else:
    for r in range(n-2):
        for c in range(m-2):
            if listA[r][c] != listB[r][c]:
                cnt += 1
                check(r, c)

if cnt != -1:
    if listA != listB: # A와 B가 같은지 확인
        cnt = -1
print(cnt)