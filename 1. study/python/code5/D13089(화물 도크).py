import sys
sys.stdin = open('D13089.txt')
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     meet = []
#     for i in range(N):
#         s, e = map(int, input().split())
#         meet.append([s, e])
#
#     meet.sort(key = lambda x: x[1]) # 이렇게만 하면 정확하게 안 될 수 있다 ! 오로지 뒷 놈으로만 sort하다보니 순서에 따라서 틀릴 수 o
#                                     # (22, 23) (21, 23) 이렇게 될지도?
#
#     # meet = [[0,0]] + meet
#     cnt = 0
#     i = 0
#     # print(meet)
#     for j in range(1, N):
#         if meet[i][1] <= meet[j][0]:
#             cnt += 1
#             i = j
#     print(f'#{tc} {cnt + 1}')

#---------------------------------------------
# 교수님 풀이
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # def cmp(x): # 이거랑 같은 것임
    #     return x[1], x[0]

    arr.sort(key = lambda x: (x[1], x[0])) # 이렇게 해줘야 됨

    finish = ans = 0
    for i in range(N):
        if finish <= arr[i][0]:
            ans += 1
            finish = arr[i][1]

    print(f'#{tc} {ans}')

