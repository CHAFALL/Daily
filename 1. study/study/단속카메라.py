def solution(routes):
    answer = 1

    N = len(routes)

    # 진출 구간 오름차순 정렬
    routes.sort(key=lambda x: x[-1])

    end = routes[0][1]  # 감시 카메라 범위의 끝
    for i in range(1, N):
        if end < routes[i][0]:
            answer += 1
            end = routes[i][1]

    return answer

print(solution([[-20,-15], [-14,-5], [-18,-13], [-5,-3]]))


# 감시 카메라의 범위 갱신해주는 문제 -> 갱신하면서 카메라 수 증가 시키기




