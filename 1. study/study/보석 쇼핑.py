def solution(gems):

    gems_set = set(gems)
    N = len(gems)
    M = len(gems_set) # 보석 종류의 수
    # 초기 세팅
    start = 0
    end = 0
    gems_dic = {}
    min_value = 999

    while end < N:
        # 내 보석 사전에 기존에 없을 시
        if gems[end] not in gems_dic:
            gems_dic[gems[end]] = 1
        # 기존에 있을 시
        else:
            gems_dic[gems[end]] += 1

        end += 1

        # 모든 종류가 내 사전에 있을 시
        if len(gems_dic) == M:
            while start < end:
                # 맨 앞놈 보석 종류의 보석이 2개 이상이면 빼도 문제 없자너.
                if gems_dic[gems[start]] > 1:
                    gems_dic[gems[start]] -= 1

                    start += 1

                elif end - start < min_value:
                    min_value = end - start
                    answer = [start + 1, end]  # 1부터 시작이므로
                    break
                else:
                    break


    return answer

# 경이롭다 이 문제!!! (진짜 좋다.)
# gems[end] not in gems_dic: .key 라고 안 해도 되는 구나
# len(gems_dic) 이것이 가능한 것도 처음 암

print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))


