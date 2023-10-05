import sys
sys.stdin = open('D5644.txt')

# # 제자리, 상, 우, 하, 좌
# dy = [0, -1, 0, 1, 0]
# dx = [0, 0, 1, 0, -1]
#
# T = int(input())
# for tc in range(1, T + 1):
#     # 총 이동시간, BC의 개수
#     M, A = map(int, input().split())
#     move_A = list(map(int, input().split()))
#     move_B = list(map(int, input().split()))
#     # 위치(0, 1), 범위(2), 성능(3)
#     BC = [list(map(int, input().split())) for _ in range(A)]
#     # 초기 플레이어 위치
#     p1x, p1y = 1, 1
#     p2x, p2y = 10, 10
#     ans = 0
#     for i in range(M):
#         # 충전 가능한 리스트
#         charge_A = []
#         charge_B = []
#         for j in range(A):
#             # BC 영역에 속하는 지 확인하기
#             if abs(p1x - BC[j][0]) + abs(p1y - BC[j][1]) <= BC[j][2]:
#                 charge_A.append((BC[j][3], j))  # 인덱스도 넣은 이유? 똑같은 파워가진 놈도 인풋보니깐 있길래
#             if abs(p2x - BC[j][0]) + abs(p2y - BC[j][1]) <= BC[j][2]:
#                 charge_B.append((BC[j][3], j))
#
#
#         # (완전 탐색)(이렇게 쓰면 a가 없으면 안 돌아가겠네)
#         max_v = 0
#         for p1, idx1 in charge_A:
#             temp = 0
#             for p2, idx2 in charge_B:
#                 temp += p1
#                 # 충전하는 BC가 다를 때만 더해줌
#                 if idx1 != idx2:
#                     temp += p2
#             if max_v < temp:
#                 max_v = temp
#         ans += max_v
#
#         # 플레이어 이동
#         p1x += dx[move_A[i]]
#         p1y += dy[move_A[i]]
#         p2x += dx[move_B[i]]
#         p2y += dy[move_B[i]]
#
#     print(f'#{tc} {ans}')

#====================================================================
# 제자리, 상, 우, 하, 좌
dy = [0, -1, 0, 1, 0]
dx = [0, 0, 1, 0, -1]

T = int(input())
for tc in range(1, T + 1):
    # 총 이동시간, BC의 개수
    M, A = map(int, input().split())
    move_A = list(map(int, input().split()))
    move_B = list(map(int, input().split()))
    # 위치(0, 1), 범위(2), 성능(3)
    BC = [list(map(int, input().split())) for _ in range(A)]
    # 초기 플레이어 위치
    p1x, p1y = 1, 1
    p2x, p2y = 10, 10
    ans = 0
    for i in range(M + 1):
        # 충전 가능한 리스트
        charge_A = []
        charge_B = []
        for j in range(A):
            # BC 영역에 속하는 지 확인하기
            if abs(p1x - BC[j][0]) + abs(p1y - BC[j][1]) <= BC[j][2]:
                charge_A.append((BC[j][3], j))  # 인덱스도 넣은 이유? 똑같은 파워가진 놈도 인풋보니깐 있길래
            if abs(p2x - BC[j][0]) + abs(p2y - BC[j][1]) <= BC[j][2]:
                charge_B.append((BC[j][3], j))

        charge_A.append((0, -1)) # 없으면 for문 자체가 안 돌아가는 것 방지
        charge_B.append((0, -1))


# 이렇게 하면 p2가 값이 여러개 일 때 값이 다 더해짐
# 해결
        # (완전 탐색)
        max_v = 0
        for p1 in charge_A:
            temp = p1[0]
            for p2 in charge_B:
                if p1 != p2:
                    temp2 = p2[0]
                else:
                    temp2 = 0
                if max_v < temp + temp2:
                    max_v = temp + temp2
        ans += max_v

        if i == M:
            break
        # 플레이어 이동
        p1x += dx[move_A[i]]
        p1y += dy[move_A[i]]
        p2x += dx[move_B[i]]
        p2y += dy[move_B[i]]

    print(f'#{tc} {ans}')
#---------------------------------------------------------------------------------
# # 제자리, 상, 우, 하, 좌
# dy = [0, -1, 0, 1, 0]
# dx = [0, 0, 1, 0, -1]
#
# T = int(input())
# for tc in range(1, T + 1):
#     # 총 이동시간, BC의 개수
#     M, A = map(int, input().split())
#     move_A = list(map(int, input().split()))
#     move_B = list(map(int, input().split()))
#     # 위치(0, 1), 범위(2), 성능(3)
#     BC = [list(map(int, input().split())) for _ in range(A)]
#     # 초기 플레이어 위치
#     p1x, p1y = 1, 1
#     p2x, p2y = 10, 10
#     ans = 0
#     for i in range(M + 1):
#         # 충전 가능한 리스트
#         charge_A = []
#         charge_B = []
#         for j in range(A):
#             # BC 영역에 속하는 지 확인하기
#             if abs(p1x - BC[j][0]) + abs(p1y - BC[j][1]) <= BC[j][2]:
#                 charge_A.append((BC[j][3], j))  # 인덱스도 넣은 이유? 똑같은 파워가진 놈도 인풋보니깐 있길래
#             if abs(p2x - BC[j][0]) + abs(p2y - BC[j][1]) <= BC[j][2]:
#                 charge_B.append((BC[j][3], j))
#
#         charge_A.sort(reverse = True)
#         charge_B.sort(reverse = True)
#
#         # (완전 탐색)
#         temp1, used = 0, -1
#         for P, idx in charge_A:
#             used = idx
#             temp1 += P
#             break
#         for P, idx in charge_B:
#             if used != idx:
#                 temp1 += P
#                 break
#
#         # 2번 사용자 먼저 선택하는 경우
#         temp2, used = 0, -1
#         for P, idx in charge_B:
#             used = idx
#             temp2 += P
#             break
#         for P, idx in charge_A:
#             if used != idx:
#                 temp2 += P
#                 break
#         ans += max(temp1, temp2)
#
#         if i == M:
#             break
#         # 플레이어 이동
#         p1x += dx[move_A[i]]
#         p1y += dy[move_A[i]]
#         p2x += dx[move_B[i]]
#         p2y += dy[move_B[i]]
#
#     print(f'#{tc} {ans}')
