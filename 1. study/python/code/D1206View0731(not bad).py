import sys
sys.stdin = open('D1206')
# 이렇게 풀면 안되는 이유!! 젤 위의 것만 처리됨(2차원을 1차원으로 푼 느낌)

# T = 10
# for tc in range(1, T+1):
#     N = int(input())
#     arr = list(map(int, input().split()))
#
#
#     count = 0
#     for i in range(2, N-2): # 인덱스 0부터 시작함을 주의
#         is_view = True
#         for j in [i-2, i-1, i+1, i+2]:
#             if arr[i] <= arr[j]:
#                 is_view = False
#                 break
#
#         if is_view:
#             count += 1
#
#     print(count)


#```````````````````````````````````````````````````````````````````````````````
T = 10
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))


    count = 0
    for i in range(2, N-2): # 인덱스 0부터 시작함을 주의
        max_v = 0
        for j in [i-2, i-1, i+1, i+2]:
            if max_v <= arr[j]:
                max_v = arr[j]


        if arr[i] > max_v:
            count += arr[i] - max_v

    print(count)







