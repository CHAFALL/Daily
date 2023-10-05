import sys
sys.stdin = open('D1244.txt')

# # 선택 정렬을 해서 젤 큰 것이랑 앞의 것이랑 바꾸도록 하고
# # 만약에 max 값이 된다면 그때부터는 끝에 2개만 계속 바꾸는 방식
#
# T = int(input())
#
#
# def selectionSort():
#     global cnt
#
#     for i in range(N - 1):
#         # 정렬이 덜 되더라도 N만큼 바꿨으면 나옴
#         if cnt == C:
#             return
#         max_idx = i
#         for j in range(i + 1, N):
#             if nums[max_idx] <= nums[j]:  # = 달아줘야 됨(하지만 이걸로 인한 문제점이 또 발생)(아예 안 바꾸고 넘어가야 되는데 티는 안 나지만 바꿈)(카운트 되어버림)
#                 max_idx = j
#         # 무조건 i번과 바꿈(자기자신도)
#         nums[i], nums[max_idx] = nums[max_idx], nums[i]
#         cnt += 1
#
#     return
#
#
# for tc in range(1, T + 1):
#     nums, C = input().split()
#     nums = list(map(int, nums))
#     C = int(C)
#     N = len(nums)
#     cnt = 0
#     # 선택 정렬
#     selectionSort()
#     # 최대값으로 정렬이 되었으면 그 이후부터는 맨 끝 값 2개끼리 바꾸기
#     # 정렬이 다 되어도 카운트가 남아있는 경우
#     while cnt != C:
#         nums[-2], nums[-1] = nums[-1], nums[-2]
#         cnt += 1
#
#     print(f"#{tc} {''.join(str(num) for num in nums)}")
#---------------------------------------------------------------------------------------------------------------------------
# # 틀린 이유: 똑같은 숫자가 있으면 똑같은 숫자끼리 바꿔주면 되는거네 (뒤에 2개랑 바꿀 필요도 없고)(15개 중 13개 맞음)
#
# T = int(input())
#
#
# def selectionSort():
#     global cnt
#
#     for i in range(N - 1):
#         # 정렬이 덜 되더라도 N만큼 바꿨으면 나옴
#         if cnt == C:
#             return
#         max_idx = i
#         for j in range(N - 1, i, -1): # 뒤에서부터 탐색하지 뭐
#             if nums[max_idx] < nums[j]:
#                 max_idx = j
#
#         # 바꾸기 전에 i가 max_idx면 넘어가기!(cnt 카운트 안하기 위해)
#         if i == max_idx:
#             continue
#         nums[i], nums[max_idx] = nums[max_idx], nums[i]
#         cnt += 1
#
#     return
#
#
# for tc in range(1, T + 1):
#     nums, C = input().split()
#     nums = list(map(int, nums))
#     C = int(C)
#     N = len(nums)
#     cnt = 0
#     # 선택 정렬
#     selectionSort()
#     # 최대값으로 정렬이 되었으면 그 이후부터는 맨 끝 값 2개끼리 바꾸기
#     # 정렬이 다 되어도 카운트가 남아있는 경우
#
#     while cnt != C:
#         nums[-2], nums[-1] = nums[-1], nums[-2]
#         cnt += 1
#
#     print(f"#{tc} {''.join(str(num) for num in nums)}")

#-----------------------------------------------------------------------------------------------------------------------------
# 위의 것 보완(15개중 14개 맞음)
# T = int(input())
#
#
# def selectionSort():
#     global cnt
#
#     for i in range(N - 1):
#         # 정렬이 덜 되더라도 N만큼 바꿨으면 나옴
#         if cnt == C:
#             return
#         max_idx = i
#         for j in range(N - 1, i, -1): # 뒤에서부터 탐색하지 뭐
#             if nums[max_idx] < nums[j]:
#                 max_idx = j
#
#         # 바꾸기 전에 i가 max_idx면 넘어가기!(cnt 카운트 안하기 위해)
#         if i == max_idx:
#             continue
#         nums[i], nums[max_idx] = nums[max_idx], nums[i]
#         cnt += 1
#
#     return
#
#
# for tc in range(1, T + 1):
#     nums, C = input().split()
#     nums = list(map(int, nums))
#     C = int(C)
#     N = len(nums)
#     cnt = 0
#     # 선택 정렬
#     selectionSort()
#     # 최대값으로 정렬이 되었으면 그 이후부터는 맨 끝 값 2개끼리 바꾸기
#     # 정렬이 다 되어도 카운트가 남아있는 경우
#
#     # 중복이 있다면 바로 출력
#     if len(nums) != len(set(nums)):
#         pass
#     else:
#         while cnt != C:
#             nums[-2], nums[-1] = nums[-1], nums[-2]
#             cnt += 1
#     print(f"#{tc} {''.join(str(num) for num in nums)}")

#---------------------------------------------------------------------------------------------------------------------
def dfs(n, k, prize):
    global ans
    money = int("".join(prize))

    # 해봤던 것은 다시 해볼 필요가 없다.(단, 교환횟수도 필요)
    if (money, k) in visited:  # 메모이제이션
        return

    visited.append((money, k))  # visited에 추가

    if k == n:
        ans = max(ans, int(money))
        return

    for i in range(N - 1):
        for j in range(i + 1, N):
            prize[i], prize[j] = prize[j], prize[i]
            dfs(n, k + 1, prize)
            prize[i], prize[j] = prize[j], prize[i]


for tc in range(1, int(input()) + 1):
    prize, C = map(str, input().split())
    prize = list(prize)
    N = len(prize)
    visited = []  # 금액과 k
    C = int(C)

    ans = 0
    dfs(C, 0, prize)
    print(f'#{tc} {ans}')