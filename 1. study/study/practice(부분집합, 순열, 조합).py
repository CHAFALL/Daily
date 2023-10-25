# 부분집합 구하기
def powerset(k, p, s):

    if k == N:
        print(p, s)
        return
    else:
        powerset(k + 1, p + [arr[k]], s + arr[k])
        powerset(k + 1, p, s)


arr = [1,2,3,4,5,6,7]
N = len(arr)

powerset(0, [], 0)
#-----------------------------------------------------
# 부분집합(비트마스킹, 그룹 나누기)(반)(공집합 x)
arr = [1,2,3,4]
N = len(arr)
for i in range(1, 1 << (N - 1)):
    subset1 = []
    subset2 = []
    for j in range(N):
        if i & (1 << j):
            subset1.append(arr[j])
        else:
            subset2.append(arr[j])

    print(subset1, subset2)
#-----------------------------------------------------
# 순열 nPn
def perm(k, p):
    if k == N:
        print(p)
        return
    else:
        for i in range(N):
            if visited[i] == 0:
                visited[i] = 1
                perm(k + 1, p + [arr[i]])
                visited[i] = 0

arr = [1, 2, 3]
N = len(arr)
visited = [0] * N
perm(0, [])
#-------------------------------------------------
# 순열 nPr
def perm(k, p, s):
    global cnt
    if k == R:
        cnt += 1
        print(p, s, cnt)
        return
    else:
        for i in range(N):
            if not visited[i]:
                visited[i] = 1
                perm(k + 1, p + [arr[i]], s + arr[i])
                visited[i] = 0


arr = [1, 2, 3, 4, 5]
N = len(arr)
R = 3
visited = [0] * N
cnt = 0
perm(0, [], 0)
#----------------------------------------------------
# nㅠn (중복 순열)
def perm(k, p):
    if k == N:
        print(p)
        return
    else:
        for i in range(N):
            perm(k + 1, p + [arr[i]])

arr = [1, 2, 3]
N = len(arr)
perm(0, [])
#----------------------------------------------------
# nㅠr (중복순열)
def perm(k, p, s):
    if k == R:
        print(p, s)
        return
    else:
        for i in range(N):
            perm(k + 1, p + [arr[i]], s + arr[i])

arr = [1, 2, 3, 4, 5]
N = len(arr)
R = 3
perm(0, [], 0)
#-----------------------------------------------------
# 조합 nCr (중복이 없어서 가능)
def comb(k, r, p, s):
    if k == N:
        if r == R:
            print(p, s)
        return
    else:
        comb(k + 1, r + 1, p + [arr[k]], s+arr[k])
        comb(k + 1, r, p, s)

arr = [1, 2, 3, 4, 5]
N = len(arr)
R = 3
comb(0, 0, [], 0)
#-----------------------------------------------------
# 조합 nCr 재귀로
def comb(k, p, s, cur): # s: 시작숫자, cur: 현재 숫자
    if k == R:
        print(p, cur)
        return

    else:
        for i in range(s, N - R + 1 + k):
            comb(k + 1, p + [arr[i]], i + 1, cur + arr[i])


arr = [1, 2, 3, 4, 5]
N = len(arr)
R = 3
comb(0, [], 0, 0)
#-------------------------------------------
# 조합 nCr 재귀면서 중복까지
def comb(k, p, s, cur):
    if k == R:
        print(p, cur)
        return
    else:
        for i in range(N):
            comb(k + 1, p + [arr[i]], i, cur + arr[i])


arr = [1, 2, 3, 4, 5]
N = len(arr)
R = 3
comb(0, [], 0, 0)


