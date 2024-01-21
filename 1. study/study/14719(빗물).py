H, W = map(int, input().split())
arr = list(map(int, input().split()))

total = 0

# 양 끝은 물이 고일 수 없다.
for i in range(1, W - 1):
    left_max = 0
    right_max = 0

    # 현재 위치를 기준으로 좌측 최댓값 구하기
    for j in range(i):
        left_max = max(left_max, arr[j])
    # 현재 위치를 기준으로 우측 최댓값 구하기
    for j in range(i+1, W):
        right_max = max(right_max, arr[j])

    # 좌측 최댓값과 우측 최댓값 중 작은 값 구하기
    temp = min(left_max, right_max)

    # 둘러싸인 벽 중 작은 값과 현재 위치의 차이만큼 물이 고인다.(현재 위치가 더 작을 시)
    if arr[i] < temp:
        total += temp -arr[i]

print(total)


# # 슬라이싱을 통한 풀이
# H, W = map(int, input().split())
# arr = list(map(int, input().split()))
#
# total = 0
#
# # 양 끝은 물이 고일 수 없다.
# for i in range(1, W - 1):
#     # 현재 위치를 기준으로 좌측 최댓값 구하기
#     left_max = max(arr[:i])
#     # 현재 위치를 기준으로 우측 최댓값 구하기
#     right_max = max(arr[i + 1:])
#
#     # 좌측 최댓값과 우측 최댓값 중 작은 값 구하기
#     temp = min(left_max, right_max)
#
#     # 둘러싸인 벽 중 작은 값과 현재 위치의 차이만큼 물이 고인다.(현재 위치가 더 작을 시)
#     if arr[i] < temp:
#         total += temp -arr[i]
#
# print(total)

#---------------------------------
