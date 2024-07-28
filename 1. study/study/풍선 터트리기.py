# DFS로 하기에는 길이 조건이 너무 빡셈...
# 자신의 왼쪽 혹은 오른쪽 어느 한 쪽 방향에 자기보다 큰 수만 존재할 시,
# 마지막까지 생존 가능

def solution(a):
    N = len(a)
    result = [False for _ in range(N)]

    minLeft, minRight = 1_000_000_001, 1_000_000_001

    for i in range(N):
        if a[i] < minLeft:
            minLeft = a[i]
            result[i] = True
        if a[-i-1] < minRight:
            minRight = a[-i-1]
            result[-i-1] = True

    return sum(result)

print(solution([-16,27,65,-2,58,-92,-71,-68,-61,-33]))


# def solution(a):
#     N = len(a)
#     result = [False for _ in range(N)]
#
#     minLeft, minRight = 1_000_000_001, 1_000_000_001
#
#     for i in range(N):
#         if a[i] < minLeft:
#             minLeft = a[i]
#             result[i] = True
#         if a[-i-1] < minRight:
#             minRight = a[-i-1]
#             result[-i-1] = True
#
#     return sum(result)
#
# print(solution([-16,27,65,-2,58,-92,-71,-68,-61,-33]))



# sum(result)로 가능한 갯수 파악하는 것 처음 암
