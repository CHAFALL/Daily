# 순열 이용
def perm(k, p):
    global ans
    if k == N:
        # 하고 싶은 일 하기
        ans.update([''.join(p)])
        return
    else:
        for i in range(N):
            if not visited[i]:
                if k == 0:
                    visited[i] = 1
                    perm(k + 1, p + [Text[i]])
                    visited[i] = 0  # 초기화

                # k=0이 아니면 앞의 놈과 비교
                else:
                    if Text[i] != p[k - 1]:
                        visited[i] = 1
                        perm(k + 1, p + [Text[i]])
                        visited[i] = 0  # 초기화


Text = input()
N = len(Text)
visited = [0] * N
ans = set()
perm(0, [])
print(len(ans))
