'''
2
5
3 2
1 4
4 1
2 3
5 5
7
3 6
7 3
4 2
1 4
5 7
2 5
6 1
'''
# 다른 참가자보다 다 덜 떨어진 놈은 제거.
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = []
    for _ in range(N):
        A, B = map(int, input().split())
        arr.append((A, B))

    arr.sort(key=lambda x: x[0])
    cnt = 1
    superior = arr[0][1]

    for i in range(1, N):
        if superior > arr[i][1]:
            superior = arr[i][1]
            cnt += 1

    print(cnt)

# for문 2개면 그냥 풀리겠지만(break포함) 런타임 뜰 듯.
# 둘 다 순위가 좀 높은 놈이 있다면 우르르 떨어질 듯.
# 순위의 합이 작은 놈을 찾을까?,
# 정렬을 한 번 해서(A기준.) (B로만 판단)
# A기준은 판단 안 해도 되는 이유: 이미 잘난 애들을 먼저 세워놓았으므로
# (서류 잘 친 애들 순..)