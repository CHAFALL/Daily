'''
1
2 3
1 2 3
4 5 6
'''

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [[0] * (M+2)] + [[0] + list(map(int, input().split())) +[0] for _ in range(N)] + [[0] * (M+2)]

    print(arr) # [[0, 0, 0, 0, 0], [0, 1, 2, 3, 0], [0, 4, 5, 6, 0], [0, 0, 0, 0, 0]]