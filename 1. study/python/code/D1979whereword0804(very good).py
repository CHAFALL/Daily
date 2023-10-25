import sys
sys.stdin = open('D1979')

T = int(input())
for tc in range(1, T+1):
    N, K =map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # K개 초과짜리일 때도 카운트 되는 것 고려 필요
    #1 1 1이 나와있고 바로 다음에 0이 나오는 순간만 count하면 될 듯
    # 여기서 마지막에 1 1 1이 되고 0으로 마무리 되지 않으면 또 카운트가 안됨
    total_counts = 0
    for i in range(N):
        counts = 0
        for j in range(N):
            if arr[i][j] == 1:
                counts += 1
            # 마지막일 때와 0이 될 때 counts와 K 비교
            if j == N-1 or arr[i][j] == 0:
                if counts == K:
                    total_counts += 1
                counts = 0

    for j in range(N):
        counts = 0
        for i in range(N):
            if arr[i][j] == 1:
                counts += 1
            if i == N - 1 or arr[i][j] == 0:
                if counts == K:
                    total_counts += 1
                counts = 0

    print(total_counts)

#```````````````````````````````````````````````````````````
# # 이렇게 짜면 1 1 1 0 1 일때는 카운트가 안됨
# T = int(input())
# for tc in range(1, T+1):
#     N, K =map(int, input().split())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#
#     total_counts = 0
#     for i in range(N):
#         counts = 0
#         for j in range(N):
#             if arr[i][j] == 1:
#                 counts += 1
#             # 0을 만나면 초기화
#             else:
#                 counts = 0
#         if counts ==K:
#             total_counts +=1
#
#     for j in range(N):
#         counts = 0
#         for i in range(N):
#             if arr[i][j] == 1:
#                 counts += 1
#             # 0을 만나면 초기화
#             else:
#                 counts = 0
#         if counts ==K:
#             total_counts +=1
#
#     print(total_counts)


