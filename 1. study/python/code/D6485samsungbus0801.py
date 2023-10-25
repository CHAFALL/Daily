import sys
sys.stdin = open('D6485')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    counts_table = [0] * (5000+1)

    for _ in range(N):
        A, B = map(int, input().split())
        # 카운팅
        for i in range(A, B+1):
            counts_table[i] += 1

    P = int(input())
    print(f'#{tc}', end =' ') #print 위치 잘 볼 것 이렇게 하기 싫으면 아래 방식대로 ㄱㄱ
    for _ in range(P):
        C = int(input())

        print(counts_table[C], end=' ')

    print()



# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     counts = [0] * 5001
#
#     # 카운팅
#     for i in range(N):
#         S, E = map(int, input().split())
#         for j in range(S, E+1):
#             counts[j] +=1
#
#     # 각 정류장에 몇개의 버스 노선이 운행
#     P = int(input())
#     ans = []
#     for _ in range(P):
#         p = int(input())
#         ans.append(counts[p])
#
#     print(f'#{tc}', *ans)