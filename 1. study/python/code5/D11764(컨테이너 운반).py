import sys
sys.stdin = open('D11764.txt')

# def solve():
#     i = 0
#     j = 0
#     total = 0
#     while i < M and j < N:
#         # 젤 큰 트럭이 현재 젤 큰 무게를 감당할 수 있으면 가져감
#         if truck[i] >= container[j]:
#             total += container[j]
#             i += 1
#             j += 1
#         # 젤 큰 무게 감당 못하면 다음으로 큰 무게로 넘어감
#         # 젤 큰 트럭이 남은 컨테이너들을 모두 감당 못하면 끝
#         else:
#             j += 1
#
#     return total
#
# T = int(input())
# for tc in range(1, T+1):
#     # N 컨테이너 수, M 트럭 수
#     N, M = map(int, input().split())
#     container = list(map(int, input().split()))
#     truck = list(map(int, input().split()))
#
#     container.sort(reverse= True)
#     truck.sort(reverse= True)
#
#     print(f'#{tc} {solve()}')
#---------------------------------------------------------------
#교수님 풀이

T = int(input())
for tc in range(1, T+1):
    # N 컨테이너 수, M 트럭 수
    N, M = map(int, input().split())
    container = list(map(int, input().split()))
    truck = list(map(int, input().split()))

    container.sort(reverse= True)
    truck.sort(reverse= True)

    i = j = ans = 0
    while i < M and j < N:
        # 젤 큰 트럭이 현재 젤 큰 무게를 감당할 수 있으면 가져감
        if truck[i] >= container[j]:
            ans += container[j]
            i += 1
            j += 1
        # 젤 큰 무게 감당 못하면 다음으로 큰 무게로 넘어감
        # 젤 큰 트럭이 남은 컨테이너들을 모두 감당 못하면 끝
        else:
            j += 1
    print(f'#{tc} {ans}')