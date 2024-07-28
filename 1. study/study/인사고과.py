# 전에 유사한 것 푼 적이 있는데 기억이 조금 남.

# 내 기억에 둘 중 하나는 내림차순으로 해야 했던 걸로 기억
# 그럼 알아서 하나는 정리 되었던 걸로 기억
# 최대값을 알 수 있는 변수도 하나 필요했던 걸로 기억

def solution(scores):
    answer = 1

    target_a, target_b = scores[0]
    target_sum = sum(scores[0])



    # 첫 번째 점수에 대해 내림차순
    # (동일시 두 번째 점수에 대해 오름차순) (중요!!)
    # max_a에 동일한 것이 있을 때에 대한 처리를 위해 필요
    # 낮은 것 먼저 시작해줘야 됨.

    # 이러면 b값만 신경써주면 된다!!

    scores.sort(key=lambda x: (-x[0], x[1]))
    # [[3, 2], [3, 2], [2, 1], [2, 2], [1, 4]]

    max_b = 0


    for a, b in scores:
        # 인셉티브 탈락 조건
        if target_a < a and target_b < b:
            return -1

        # 인셉티브 통과한 애들 중에
        if b >= max_b:
            max_b = b # 갱신
            if a + b > target_sum:
                answer += 1

    return answer


print(solution([[2,2],[1,4],[3,2],[3,2],[2,1]]))