
def solution(genres, plays):

    N = len(genres)
    total = []
    genres_total = {} # 각 장르별 총합

    # 장르 와 플레이 수 통합시키기
    for i in range(N):
        total.append((genres[i], plays[i], i))  # 장르, 플레이 수, 인덱스


    for i in range(N):
        # 장르가 딕셔너리에 없다면 새로 생성
        if total[i][0] not in genres_total.keys():
            genres_total[total[i][0]] = total[i][1]
        # 장르가 딕셔너리에 있다면 추가
        else:
            genres_total[total[i][0]] += total[i][1]

    genres_total = list(genres_total.items()) # 리스트로 변환
    genres_total.sort(key = lambda x: (-x[1]))

    total.sort(key=lambda x: (x[0], -x[1], x[2]))

    answer = []
    # 곡이 하나만 있을 수 있음. -> count 방식으로 2개가 될 때마다 나와주기(하나는 반드시 있음)
    for gnrs_ttl in genres_total:
        cnt = 0
        for ttl in total:
            if gnrs_ttl[0] == ttl[0]:
                if cnt != 2:
                    cnt += 1
                    answer.append(ttl[2])
                else:
                    break

    return answer


print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))

#------------------
def solution(genres, plays):
    answer = []

    dic1 = {}
    dic2 = {}

    for i, (g, p) in enumerate(zip(genres, plays)):
        if g not in dic1:
            dic1[g] = [(i, p)]
        else:
            dic1[g].append((i, p))

        if g not in dic2:
            dic2[g] = p
        else:
            dic2[g] += p

    for (k, v) in sorted(dic2.items(), key=lambda x:x[1], reverse=True):
        for (i, p) in sorted(dic1[k], key=lambda x:x[1], reverse=True)[:2]:
            answer.append(i)

    return answer

