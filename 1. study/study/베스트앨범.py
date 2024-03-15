
def solution(genres, plays):

    N = len(genres)
    total = []
    genres_total = {} # 각 장르별 총합

    for i in range(N):
        total.append((genres[i], plays[i], i))  # 장르, 플레이 수, 인덱스

    total.sort(key = lambda x: (x[0], -x[1], x[2]))

    for i in range(N):
        # 장르가 딕셔너리에 없다면
        if total[i][0] not in genres_total.keys():
            genres_total[total[i][0]] = total[i][1]
        else:
            genres_total[total[i][0]] += total[i][1]

    genres_total = list(genres_total.items()) # 리스트로 변환
    genres_total.sort(key = lambda x: (-x[1]))

    print(genres_total)
    # 곡이 하나만 있을 수 있음.

    answer = []
    return answer




#---------
# def solution(genres, plays):
#     answer = []
#     temp = []
#     total_genre_d = {}
#
#     temp = [[genres[i], plays[i], i] for i in range(len(genres))]  # [장르, 재생횟수, 고유 번호] 리스트
#     temp = sorted(temp, key=lambda x: (x[0], -x[1], x[2]))  # 많이 재생될수록, 같다면 고유번호가 낮을수록
#
#     for g in temp:  # {장르 : 총 재생횟수} 딕셔너리 생성
#         if g[0] not in total_genre_d:
#             total_genre_d[g[0]] = g[1]
#         else:
#             total_genre_d[g[0]] += g[1]
#
#     total_genre_d = sorted(total_genre_d.items(), key=lambda x: -x[1])  # 재생횟수가 많은 순서로 장르 정렬
#
#     for i in total_genre_d:  # 같은 장르 내에서는 최대 2곡까지 조건대로 수록
#         count = 0
#         for j in temp:
#             if i[0] == j[0]:
#                 count += 1
#                 if count > 2:
#                     break
#                 else:
#                     answer.append(j[2])
#
#     return answer


#------------------
# def solution(genres, plays):
#     answer = []
#
#     dic1 = {}
#     dic2 = {}
#
#     for i, (g, p) in enumerate(zip(genres, plays)):
#         if g not in dic1:
#             dic1[g] = [(i, p)]
#         else:
#             dic1[g].append((i, p))
#
#         if g not in dic2:
#             dic2[g] = p
#         else:
#             dic2[g] += p
#
#     for (k, v) in sorted(dic2.items(), key=lambda x:x[1], reverse=True):
#         for (i, p) in sorted(dic1[k], key=lambda x:x[1], reverse=True)[:2]:
#             answer.append(i)
#
#     return answer

#----
# def solution(genres, plays):
#     answer = []
#     total = {}  # 장르별 총 재생횟수
#     gen_dic = {}  # 장르별 [재생횟수&고유번호]
#
#     for i in range(len(genres)):
#         genre = genres[i]
#         play = plays[i]
#         if genres[i] in total.keys():
#             total[genres[i]] += plays[i]
#             gen_dic[genres[i]].append((plays[i], i))
#         else:
#             total[genres[i]] = plays[i]
#             gen_dic[genre] = [(play, i)]
#
#     total = sorted(total.items(), key=lambda x: x[1], reverse=True)
#
#     # print(total)
#     # print(gen_dic)
#
#     for key in total:
#         playlist = gen_dic[key[0]]
#         playlist = sorted(playlist, key=lambda x: x[0], reverse=True)
#         for i in range(len(playlist)):
#             if i == 2:
#                 break
#             answer.append(playlist[i][1])
#
#         # print(playlist)
#     return answer