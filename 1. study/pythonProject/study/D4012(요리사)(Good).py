import sys
sys.stdin = open('D4012.txt')
# def comb(k, p, s): # 깊이, 재료리스트, 시작점
#     global min_v
#     if k == R:
#         # 반대쪽 재료 리스트 구성하기
#         other_p = list(set(ALL) - set(p))
#         # 재료 시너지 분석
#         temp1 = temp2 = 0
#         for i in range(R):
#             for j in range(R):
#                 temp1 += arr[p[i]][p[j]]
#                 temp2 += arr[other_p[i]][other_p[j]]
#         # 두 요리 맛 차이의 최소값 구하기
#         min_v = min(min_v, abs(temp1 - temp2))
#         return
#     else:
#         # 조합
#         for i in range(s, N - R + 1 + k):
#             comb(k + 1, p + [i], i + 1)
#
# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     R = N // 2
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     ALL = [i for i in range(N)]
#     min_v = 99999999999
#     comb(0, [], 0)
#     print(f'#{tc} {min_v}')


#--------------------------------------------------------------
def dfs(k, A, B): # 깊이, A팀, B팀
    global min_v

    if min_v == 0:
        return
    if k == N:
        if len(A) == len(B): # 같은 양으로 재료 선정했을 시
            taste_A = taste_B = 0
            for i in range(M):
                for j in range(M):
                    taste_A += arr[A[i]][A[j]]
                    taste_B += arr[B[i]][B[j]]

            min_v = min(min_v, abs(taste_A - taste_B))
        return

    else:
        dfs(k + 1, A + [k], B)  # A팀 선택
        dfs(k + 1, A, B + [k])  # B팀 선택


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    M = N // 2
    arr = [list(map(int, input().split())) for _ in range(N)]
    min_v = 99999999999
    dfs(0, [], [])
    print(f'#{tc} {min_v}')