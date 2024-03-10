


# 부분집합(비트마스킹, 그룹 나누기)(반)(공집합 x)
# arr = [1,2,3,4]
# N = len(arr)
# for i in range(1, 1 << (N - 1)):
#     subset1 = []
#     subset2 = []
#     for j in range(N):
#         if i & (1 << j):
#             subset1.append(arr[j])
#         else:
#             subset2.append(arr[j])
#
#     print(subset1, subset2)



# 부분집합 전체에서 부터 점차 줄어드는 식으로 해서 구하기
# break 걸면 시간 단축
# 짧은 놈이 긴 놈에 있는 지를 판단할 것
# 긴 놈은 짧은 놈의 접두사가 될 수 x



# 부분집합 구하기
def powerset(k, p):

    if k == N:
        print(p)
        return
    else:
        powerset(k + 1, p + [arr[k]])
        powerset(k + 1, p)

N = int(input())
arr = [input() for _ in range(N)]

powerset(0, [])