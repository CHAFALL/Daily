# # 큰 놈은 큰 놈끼리 최대한 놀자!
# def solution(A, B):
#     answer = 0
#
#     N = len(A)
#
#     A.sort(reverse=True)
#     B.sort(reverse=True)
#
#
#
#     i = 0
#     j = 0
#     while True:
#         if A[i] < B[j]:
#             i += 1
#             j += 1
#             answer += 1
#
#         # 더 작은 놈중에서 이길 수 있는 놈이 있나 찾기
#         else:
#             i += 1
#
#         if i == N or j == N:
#             break
#
#     return answer
#
# print(solution([5,1,3,7], [2,2,6,8]))


#---
# 큰 놈은 큰 놈끼리 최대한 놀자!
def solution(A, B):
    answer = 0

    N = len(A)

    A.sort(reverse=True)
    B.sort(reverse=True)

    i = 0
    j = 0
    while i < N:
        if A[i] < B[j]:
            i += 1
            j += 1
            answer += 1

        # 더 작은 놈중에서 이길 수 있는 놈이 있나 찾기
        else:
            i += 1

    return answer

print(solution([5,1,3,7], [2,2,6,8]))