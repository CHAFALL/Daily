def solution(n, stations, w):
    answer = 0
    idx = n  # 지금 내 위치

    block = 1 + (2 * w)               # 5g 기지국 전파 범위
    while idx > 0:
        bonus = 0 if len(stations) == 0 else stations.pop() # 기존의 기지국을 가져온다.

        size = idx # 전파가 닿지 않는 범위

        if bonus:  # 기지국이 있다면
            size = idx - (bonus + w)  # 내위치에서 전파국 범위를 제외하는 것이 size

        answer += size // block  # block으로 나눈 몫만큼 더한다.
        answer += (0 if size % block == 0 else 1) # 나머지가 있다면 기지국을 1개 더 설치
        print('size, block',size, block)
        print(size//block, size % block)

        idx = bonus - w - 1 # 설치한 기지국의 전파 범위를 제외하고 현 위치 갱신ㅌ

    return answer
solution(11, [4, 11], 1)