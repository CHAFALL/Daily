import sys
sys.stdin = open('D1953.txt')




pipe1 = []
pipe2 = []
pipe3 = []
pipe4 = []
pipe5 = []
pipe6 = []
pipe7 = []

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

T = int(input())
for tc in range(1, T+1):
    N, M, r, c, hour = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]


