'''
3 4
0000
0010
0000
1001
1011
1001
'''

# 만약에 불가능한 것이 있으면 -1을 출력.
N, M = map(int, input().split())

arr1 = [list(map(int, input())) for _ in range(N)]
arr2 = [list(map(int, input())) for _ in range(N)]

for i in range(N - 2):
    for j in range(M - 2):


# 같은 곳은 두번 이상 뒤집는 것은 의미 없으니깐
# 뒤집을지 말지만 판단 해주면 될 듯.
# 뒤집을 때마다 카운트