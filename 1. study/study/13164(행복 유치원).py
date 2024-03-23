N, K = map(int, input().split()) # N: 원생 수, K: 나눌 조의 수
arr = list(map(int, input().split()))
# sort는 이미 되어있는 상태임
# 조합은 터질 듯, 인접한 원생들의 간격을 이용?
# 간격끼리 또 묶으면 또 하나의 덩어리.
# 큰 거는 되도록 혼자가 되도록 묶어야 하고?

gap = []
for i in range(N - 1):
    gap.append(arr[i+1]-arr[i])

# gap이 적은 것끼리 묶기 위함
gap.sort(reverse=True)

total = 0
for i in range(K - 1, N - 1):
    total += gap[i]

print(total)

#----------------------------------

N, K = map(int, input().split()) # N: 원생 수, K: 나눌 조의 수
arr = list(map(int, input().split()))

gap = []
for i in range(N - 1):
    gap.append(arr[i+1]-arr[i])

# gap이 적은 것끼리 묶기 위함
gap.sort()

total = 0
for i in range(K):
    total += gap[i]

print(total)
