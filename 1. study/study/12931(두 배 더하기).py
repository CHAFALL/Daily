# N = int(input())
# arr_A = [0] * N
# arr_B = list(map(int, input().split()))
#
# arr_B.sort()  # 작은 놈 먼저 집중 공략
#
#
# cnt = 0
# while True:
#     if arr_B == arr_A:
#         print(cnt)
#         break
#
#     # 2로 나눌 때 0이나 1인 배열이 있으면 안됨(즉 2이상이어야 나눌 수 있다.)
#     if arr_B[0] >= 2:
#         cnt += 1
#         for i in range(N):
#             arr_B[i] //= 2
#
#     else:
#         for i in range(N):
#             # 1빼기
#             if arr_B[i] > 0:
#                 arr_B[i] -= 1
#                 cnt += 1
#
# # 이렇게 하니깐 홀수일 때를 고려 못하는구나

#--------------------------------------------------
# N = int(input())
# arr_A = [0] * N
# arr_B = list(map(int, input().split()))
#
# arr_B.sort()  # 작은 놈 먼저 집중 공략
#
#
# cnt = 0
# while True:
#     if arr_B == arr_A:
#         print(cnt)
#         break
#
#     # 젤 작은 놈이 2이상이고 홀수가 아니어야 한다.
#     if arr_B[0] >= 2 and arr_B[0] % 2 == 0:
#         cnt += 1
#         for i in range(N):
#             arr_B[i] //= 2
#
#     else:
#         for i in range(N):
#             # 1빼기
#             if arr_B[i] > 0:
#                 arr_B[i] -= 1
#                 cnt += 1
#

#-------------------------------------------------

# 딴 거도 홀수이면 2로 못 나누구나!!! 결국 다 체크 해야 되겠네
# flag를 쓰자

# N = int(input())
# arr_A = [0] * N
# arr_B = list(map(int, input().split()))
#
# arr_B.sort() # 작은 놈 먼저 고려하기(이거 안해주면 start 방식 불가)
# cnt = 0
# start = 0
# while True:
#     if arr_B == arr_A:
#         print(cnt)
#         break
#
#     flag = True
#     for i in range(start, N):
#         # 홀수 이면 반드시 1을 빼야 됨
#         if arr_B[i] % 2 == 1:
#             arr_B[i] -= 1
#             cnt += 1
#         # 자! 전부 짝수인 상태에서 가보자고
#         # 0인게 있으면 나눌 수 x (이제부턴 빼기만)
#         if arr_B[i] == 0:
#             flag = False
#             start += 1
#             break
#
#     if flag == True:
#         cnt += 1
#         for i in range(N):
#             arr_B[i] //= 2
#
#
# # # 1빼기를 먼저 해줘서 모두 짝수로 만들어주는 것이 핵심



#--------------------
# 딴 거도 홀수이면 2로 못 나누구나!!! 결국 다 체크 해야 되겠네
# flag를 쓰자 이거는 1, 1, 1 일때를 생각해보면 안되는 이유를 알 수 있다.
# flag 검토는 1빼기를 하고 난 후에 해줘야 됨
# N = int(input())
# arr_A = [0] * N
# arr_B = list(map(int, input().split()))
#
# cnt = 0
# while True:
#     if arr_B == arr_A:
#         print(cnt)
#         break
#
#     flag = True
#     for i in range(N):
#         # 0이 있으면 나누기와 빼기 다 안해
#         if arr_B[i] == 0:
#             flag = False
#             continue
#
#         # 홀수 이면 반드시 1을 빼야 됨
#         elif arr_B[i] % 2 == 1:
#             arr_B[i] -= 1
#             cnt += 1
#         # 자! 전부 짝수인 상태에서 가보자고
#
#     if flag == True:
#         cnt += 1
#         for i in range(N):
#             arr_B[i] //= 2


# 1빼기를 먼저 해줘서 모두 짝수로 만들어주는 것이 핵심


#------------------
# 딴 거도 홀수이면 2로 못 나누구나!!! 결국 다 체크 해야 되겠네
# flag를 쓰자

N = int(input())
arr_A = [0] * N
arr_B = list(map(int, input().split()))

cnt = 0
while True:
    if arr_B == arr_A:
        print(cnt)
        break

    flag = True
    for i in range(N):
        # 0이 있으면 나누기와 빼기 다 안해
        if arr_B[i] == 0:
            continue

        # 홀수 이면 반드시 1을 빼야 됨
        elif arr_B[i] % 2 == 1:
            arr_B[i] -= 1
            cnt += 1
        # 자! 전부 짝수인 상태에서 가보자고
        # flag 검토는 반드시 여기서 해줘야 됨
        if arr_B[i] == 0:
            flag = False


    if flag == True:
        cnt += 1
        for i in range(N):
            arr_B[i] //= 2


# 1빼기를 먼저 해줘서 모두 짝수로 만들어주는 것이 핵심
#---------------------------------------------------
N = int(input())
arr_A = [0] * N
arr_B = list(map(int, input().split()))

cnt = 0
start = 0
while True:
    if arr_B == arr_A:
        print(cnt)
        break

    flag = False
    for i in range(start, N):
        # 홀수 이면 반드시 1을 빼야 됨
        if arr_B[i] % 2 == 1:
            arr_B[i] -= 1
            cnt += 1
        # 자! 전부 짝수인 상태에서 가보자고
        # 아하! 이렇게 거르면 되겠네
        if arr_B[i] > 1:
            arr_B[i] //= 2
            flag = True

    if flag:
        cnt += 1

