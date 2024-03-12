T = int(input())
for _ in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    # 인덱스 차이 2로 나도록 구하기

    arr.sort()
    max_gap = 0
    for i in range(N - 2):
        max_gap = max(max_gap, abs(arr[i + 2] - arr[i]))


    print(max_gap)
#-------------
# T = int(input())
#
# for _ in range(T):
#     N = int(input())
#     arr = sorted(list(map(int, input().split())))   # 통나무 높이 오름차순 정렬
#
#     arr2 = [0] * N                          # 재배치 해줄 통나무 배열
#
#     for i in range(N):
#         if i % 2 == 0:                     # 홀수번째로 낮은 애들은 왼쪽에서부터 삽입
#             arr2[i//2] = arr[i]
#
#         else:                              # 짝수번째로 낮은 애들은 오른쪽에서부터 삽입
#             arr2[N-1-(i//2)] = arr[i]
#
#     max_diff = 0                           # 차이의 최대값 초기화
#
#     for j in range(1, N):
#         max_diff = max(abs(arr2[j-1] - arr2[j]), max_diff)     # 다 돌면서 확인
#
#     print(max_diff)
