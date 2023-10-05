# 재귀 연습
# def f(i, N):
#     if i == N:
#         print(B)
#         return
#     else:
#         B[i] = A[i]
#         f(i+1, N)
#         return
#
# N = 3
# A = [1, 2, 3]
# B = [0] * N
#
# f(0, N)
# #print(B)
#---------------------------------------------------------------------
# 부분 집합 재귀
# def f(i, N):
#     if i == N:
#         print(bit, end= ' ')
#         for j in range(N):
#             if bit[j]:
#                 print(A[j], end = ' ')
#         print()
#         return
#     else:
#         bit[i] = 1
#         f(i + 1, N)
#         bit[i] = 0
#         f(i + 1, N)
#         return
# A = [1,2,3]
# bit = [0] * 3
# f(0, 3)
#------------------------------------------------------------------------
# 부분 집합의 합 재귀
# def f(i, N):
#     if i == N:
#         print(bit, end= ' ')
#         s = 0
#         for j in range(N):
#             if bit[j]:
#                 s += A[j]
#                 print(A[j], end = ' ')
#         print(f': {s}')
#         return
#     else:
#         bit[i] = 1
#         f(i + 1, N)
#         bit[i] = 0
#         f(i + 1, N)
#         return
# A = [1,2,3]
# bit = [0] * 3
# f(0, 3)
#========================================================================
# 부분 집합의 합 재귀 2
# def f(i, N, s): # s : i-1 원소까지 부분집합의 합(포함된 원소의 합)
#     if i == N:
#         print(bit, end= ' ')
#         print(f': {s}')
#         return
#     else:
#         bit[i] = 1           # 부분집합에 A[i] 포함
#         f(i + 1, N, s+A[i])
#         bit[i] = 0          # 부분집합에 A[i] 미포함
#         f(i + 1, N, s)
#         return
#
# A = [1,2,3]
# bit = [0] * 3
# f(0, 3, 0)
#--------------------------------------------------------------------------
# 부분집합의 합(연습문제)
# def f(i, N, s, t): # s : i-1 원소까지 부분집합의 합(포함된 원소의 합)
#     global cnt     # t : 찾으려는 합
#     cnt += 1
#     if s == t:     # 이미 도달?(그만해) (뭐 뽑아낼려고 이거 따로 만든거임)
#         print(bit)
#     elif i == N:   # 남은 원소가 없는 경우
#         return
#     elif s > t:    # 더 큰 경우도 멈춰
#         return
#     else:
#         bit[i] = 1           # 부분집합에 A[i] 포함
#         f(i + 1, N, s+A[i], t)
#         bit[i] = 0          # 부분집합에 A[i] 미포함
#         f(i + 1, N, s, t)
#         return
#
# # 1 부터 10까지 원소인 집합, 부분집합의 합이 10인 경우는?
# N = 10
# A = [i for i in range(1, N+1)]
# bit = [0] * N
# cnt = 0
# f(0, N, 0, 10)
# print(cnt) # 조건에 따라 가지치기 되는 양이 바뀜을 알수있다.
#----------------------------------------------------------------------
# # 부분집합의 합(연습문제)(내가 가지고 논거)(초반에)
# def f(i, N, s): # s : i-1 원소까지 부분집합의 합(포함된 원소의 합)
#     if i == N:
#         if s == 10:
#             print(bit, end=' ')
#             for j in range(N):
#                 if bit[j]:
#                     print(A[j], end = ' ')
#             print()
#         return
#     else:
#         bit[i] = 1           # 부분집합에 A[i] 포함
#         f(i + 1, N, s+A[i])
#         bit[i] = 0          # 부분집합에 A[i] 미포함
#         f(i + 1, N, s)
#         return
#
# # 1 부터 10까지 원소인 집합, 부분집합의 합이 10인 경우는?
# N = 10
# A = [i for i in range(1, N+1)]
# bit = [0] * N
# f(0, N, 0)

#--------------------------------------------------------------------------
# # 순열 1
# def f(i, N):
#     if i == N:
#         print(A)
#     else:
#         for j in range(i, N): # 자신부터 오른쪽 끝까지
#             A[i], A[j] = A[j], A[i]
#             f(i+1, N)
#             A[i], A[j] = A[j], A[i] # 갔다가 원상복구 해줘야됨
#
# A = [1, 2, 3]
# f(0, 3)
#=============================================================================
# 거듭 제곱
def f1(b, e):
    global cnt1

    if b == 0:
         return 1
    r = 1
    for i in range(e):
        r *= b
        cnt1 += 1
    return r

def f2(b, e):
    global cnt2

    if b == 0 or e == 0:
        return 1
    if e % 2:       #홀수면
        r = f2(b, (e-1) // 2)
        cnt2 += 1
        return  r * r * b

    else:
        r = f2(b, e // 2)
        cnt2 += 1
        return r * r

cnt1 = cnt2 = 0
print(f1(2, 20), cnt1)
print(f2(2, 20), cnt2)

