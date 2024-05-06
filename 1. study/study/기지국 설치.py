def solution(n, stations, w):
    answer = 0

    N = len(stations)
    cover = 2 * w + 1 # 커버 가능 범위

    no_list = []
    # 맨 앞과 맨 뒤를 제외한 전파가 되지 않는 곳의 길이 찾기
    for i in range(1, N):
        no_list.append((stations[i] - w) - (stations[i-1] + w) - 1)

    # 맨 앞
    no_list.append(stations[0] - w - 1)
    # 맨 뒤
    no_list.append(n - (stations[N - 1] + w))

    for no in no_list:
        if no <= 0:
            continue

        # 올림을 위해
        if no % cover != 0:
            add = no // cover + 1
        else:
            add = no // cover

        answer += add

    return answer

print(solution(11, [4, 11], 1))