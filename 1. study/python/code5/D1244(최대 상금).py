import sys
sys.stdin = open('D1244.txt')

# T = int(input())
# for tc in range(1, T+1):
#     arr, N = input().split()
#     N = int(N)
#     arr = list(map(int, arr))
#     M = len(arr)
#
#     i = 0
#     while i < N and i < M:
#         max_idx = i
#         for j in range(i+1, N):
#             if arr[max_idx] < arr[j]:
#                 max_idx = j
#
#         arr[i], arr[max_idx] = arr[max_idx], arr[i]
#         i += 1
#
#     print(arr)
#
#
#     # 선택 정렬을 할껀데 (알아서 나올 듯)
#     # 정렬이 다 되었음을 어떻게 알까? 그 때부터 작은 자리 2개만 계속 바꿔주면 되는데...
#     # 작은 자리 2개만 바꾸면 안 되는 이유가 같은 숫자가 있다면 그것 끼리만 바꿔줘도 됨
#     # 아니!! 그냥 같은 숫자인 것이 있다면 바로 나와도 됨!!


#------------------------------------------------------------
# 파이썬스럽지 않게 푼 코드
# def swap(prize, i, j):  # 123 -> /1/2/3/ -> /2/1/3/ -> 213
#     # itoa
#     prize_arr = [0] * prize_len
#     for k in range(prize_len - 1, -1, -1):
#         prize_arr[k] = prize % 10
#         prize //= 10
#
#     # swap
#     prize_arr[i], prize_arr[j] = prize_arr[j], prize_arr[i]
#
#     # atoi
#     prize = 0
#     for k in range(prize_len):
#         prize = prize * 10 + prize_arr[k]
#     return prize
#
#
# def find_max(n, k, prize):  # 123 넣으면 ->
#     global ans
#     # 메모이제이션 및 가지치기
#     for i in range(720):
#         if memo[k][i] == 0: # 없으면 추가(tree의 자식 넣는 느낌)
#             memo[k][i] = prize
#             break
#         elif memo[k][i] == prize:
#             return
#
#     if n == k:
#         ans = max(ans, prize)
#
#     else:
#         for i in range(prize_len - 1):  # nC2
#             for j in range(i + 1, prize_len):
#                 find_max(n, k + 1, swap(prize, i, j))  # -> 213 나올 수 있게
#
#
# def get_length(prize):  # 숫자판 길이 구하기
#     cnt = 0
#     while prize:
#         prize //= 10
#         cnt += 1
#     return cnt
#
#
# # 숫자판 길이
# def get_length(prize):
#     cnt = 0
#     while prize:
#         prize //= 10
#         cnt += 1
#     return cnt
#
#
# T = int(input())
# for tc in range(1, T + 1):
#     prize, N = map(int, input().split())  # 숫자판, 교환횟수
#
#     memo = [[0] * 720 for _ in range(N + 1)]
#     prize_len = get_length(prize)
#     ans = 0
#     find_max(N, 0, prize)
#     print(f'#{tc} {ans}')
#-----------------------------------------------------------------
#파이썬 답게 푼 코드
def dfs(n, k, prize):
    global ans
    money = int("".join(prize))

    if (money, k) in visited:  # 메모이제이션
        return

    visited.append((money, k))  # visited에 추가

    if k == n:
        ans = max(ans, int(money))
        return

    for i in range(len(prize) - 1):
        for j in range(i + 1, len(prize)):
            prize[i], prize[j] = prize[j], prize[i]
            dfs(n, k + 1, prize)
            prize[i], prize[j] = prize[j], prize[i]


for tc in range(1, int(input()) + 1):
    prize, N = map(str, input().split())
    prize = list(prize)
    visited = []  # 금액과 k
    N = int(N)

    ans = 0
    dfs(N, 0, prize)
    print(f'#{tc} {ans}')