def solution(triangle):

    # 인덱스 에러 피하기
    triangle = [[0] + t + [0] for t in triangle]
    # 깊이 파악하기
    N = len(triangle)

    # 앞 뒤에 0을 달아줘서 (0 + 1) ~ (N - 1 + 1)
    for i in range(1, N):
        for j in range(1, i + 2):
            # 대각선 왼쪽과 오른쪽 중 더 큰 값으로 더하기
            triangle[i][j] += max(triangle[i - 1][j - 1], triangle[i - 1][j])
    answer = max(triangle[N - 1])


    return answer

print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))