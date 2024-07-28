# 판매원, 추천인, 판매한 사람, 판매 갯수
# def solution(enroll, referral, seller, amount):
#     answer = []
#
#     N, M = len(enroll), len(seller)
#
#     # 트리를 만들까 했는데 굳이 만들 필요가 없어보임.
#     # 이게 되네 ㅋㅋㅋ
#     # Sell_Info = dict(zip(seller, amount * 100)) <- 이건 왜 안됨??
#     Sell_Info = dict(zip(seller, [a * 100 for a in amount]))  # 판매한 사람 : 판매 갯수
#     People_Info = {}  # 판매원 : [추천인, 번 금액]
#     for i in range(N):
#         People_Info[enroll[i]] = [referral[i], 0]  # 튜플은 값 못 바꿈
#
#     for sell_people, sell_amount in Sell_Info.items():
#         People_Info[sell_people][1] += int(sell_amount * 0.9)
#
#         tip = int(sell_amount * 0.1)
#         ref_people = People_Info[sell_people][0]
#
#
#         while ref_people != "-":
#             if tip * 0.1 < 1:
#                 People_Info[ref_people][1] += tip
#                 break
#             People_Info[ref_people][1] += tip - int(tip * 0.1)
#             tip = int(tip * 0.1)
#             ref_people = People_Info[ref_people][0]
#
#     for people in People_Info.values():
#         answer.append(people[1])
#
#     return answer
#
# print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"], ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"], ["young", "john", "tod", "emily", "mary"], [12, 4, 2, 5, 10]))
#

#------
# 판매원, 추천인, 판매한 사람, 판매 갯수
def solution(enroll, referral, seller, amount):
    N, M = len(enroll), len(seller)

    answer = [0 for _ in range(N)]
    info = {}  # 이름(키) : 인덱스(값)
    for index, e_name in enumerate(enroll):
        info[e_name] = index

    for s, a in zip(seller, [a * 100 for a in amount]):
        while s != '-' and a > 0:
            idx = info[s]
            answer[idx] += a - a // 10
            a //= 10
            s = referral[idx]

    return answer

print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"], ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"], ["young", "john", "tod", "emily", "mary"], [12, 4, 2, 5, 10]))


