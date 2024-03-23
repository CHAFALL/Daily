def perm(N, k, M):
    if k == M:
        print(*p)
    else:
        for i in range(N):
            # if visited[i] == 0: # 방문 안 했으면 방문 체크 해주고
                # visited[i] = 1
                p[k] = arr[i]
                perm(N, k+1, M)
                # visited[i] = 0


N, M = map(int, input().split())
arr = list(range(1, N+1))

p = [0] * M
# visited = [0] * N
perm(N, 0, M)
