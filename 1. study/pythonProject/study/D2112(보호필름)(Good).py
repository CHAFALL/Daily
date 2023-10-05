import sys
sys.stdin = open('D2112.txt')

# 아래 코드가 틀린 이유: 나는 0과 1을 분리해서 풀었는데 0과 1을 혼합해서 바꿔줘야 더 적은 c가 되는 케이스가 있다.
# 우예 섞지?? 백트래킹으로 풀어야 겠다.
'''
예시
12 2 6
1 1
1 1
1 1
1 0
1 0
0 1
0 1
0 0
0 0
1 0
1 0
1 0
답은 6번째행 1을 칠하고 7번째행에 0을 칠해서 2가 나와야하지만 3이 나오는 코드가 많습니다.
'''
# import copy
# def check(arr2):
#     for j in range(W):
#         cnt = 1
#         for i in range(D - 1):
#             # 초기화 되는 것을 방지하기 위해
#             if cnt >= K:
#                 break
#             # 연속하면 카운트
#             if arr2[i][j] == arr2[i + 1][j]:
#                 cnt += 1
#             # 연속하지 않으면 초기화
#             else:
#                 cnt = 1
#         if cnt < K:
#             return 0
#     return 1
# # 부분집합?
# def powerset(k, c, p): # 깊이, 카운트, 배열
#     global min_v
#     # 가지치기
#     if min_v <= c:
#         return
#     if k == D:
#         arr2 = copy.deepcopy(arr)
#         # 하고 싶은 일
#         # 바꿔주기(1)
#         for i in p:
#             for j in range(W):
#                 arr2[i][j] = 1
#         # 체크하기
#         if check(arr2):
#             min_v = c
#             return
#
#         # 바꿔주기(0)
#         for i in p:
#             for j in range(W):
#                 arr2[i][j] = 0
#         # 체크하기
#         if check(arr2):
#             min_v = c
#             return
#
#         return
#     else:
#         # 포함 안 시키는 경우(이게 앞에 있는게 나을 것 같음 )
#         powerset(k + 1, c, p)
#         # 포함 시키는 경우
#         powerset(k + 1, c + 1, p + [k])
#
# T = int(input())
# for tc in range(1, T + 1):
#     # 두께, 가로크기, 합격기준
#     D, W, K = map(int, input().split())
#     arr = [list(map(int, input().split())) for _ in range(D)]
#     min_v = 99
#     powerset(0, 0, [])
#
#     print(f'#{tc} {min_v}')
# #


#-----------------------------------------------------------------------------------------------
import copy
def check(arr2):
    for j in range(W):
        cnt = 1
        for i in range(D - 1):
            # 초기화 되는 것을 방지하기 위해
            if cnt >= K:
                break
            # 연속하면 카운트
            if arr2[i][j] == arr2[i + 1][j]:
                cnt += 1
            # 연속하지 않으면 초기화
            else:
                cnt = 1
        if cnt < K:
            return 0
    return 1

# 부분집합?
def powerset(k, c, arr2): # 깊이, 카운트, 배열
    global min_v
    # 가지치기
    if min_v <= c:
        return
    if k == D:
        # 하고싶은 일 하기
        if check(arr2):
            min_v = c
        return
    else:
        # 포함 안 시키는 경우
        powerset(k + 1, c, arr2)
        # 포함 시키는 경우(1)
        for j in range(W):
            arr2[k][j] = 1
        powerset(k + 1, c + 1, arr2)
        # 포함 시키는 경우(0)
        for j in range(W):
            arr2[k][j] = 0
        powerset(k + 1, c + 1, arr2)
        # 초기화(해당 행만)
        for j in range(W):
            arr2[k][j] = arr[k][j]


T = int(input())
for tc in range(1, T + 1):
    # 두께, 가로크기, 합격기준
    D, W, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(D)]
    min_v = 99
    arr2 = copy.deepcopy(arr)
    powerset(0, 0, arr2)

    print(f'#{tc} {min_v}')