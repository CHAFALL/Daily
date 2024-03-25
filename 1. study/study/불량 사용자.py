def check(user, ban):
    # zip: 동일한 개수로 이루어진 자료형을 묶어줌 -> 미리 차단 필요 (문자열도 iterable 객체임)
    if len(user) != len(ban): # 길이가 다르면 비교할 필요도 없음
        return False
    else:
        for usr, bn in zip(user, ban):
            if bn == '*':
                continue
            elif usr != bn:
                return False

    return True


def perm(N, R, visited, user, ban, k, p):
    global answer
    if k == R:
        cnt = 0
        for a, b in zip(p, ban):
            if check(a, b):
                cnt += 1
        # 이걸 이렇게 처리를 하네
        # 지린다.
        if cnt == R:
            if set(p) not in answer:
                answer.append(set(p))

        return
    else:
        for i in range(N):
            if not visited[i]:
                visited[i] = 1
                perm(N, R, visited, user, ban, k + 1, p + [user[i]])
                visited[i] = 0

def solution(user_id, banned_id):
    global answer

    answer = []

    N = len(user_id)
    R = len(banned_id) # 제재 아이디 수, N개를 충족 못하면 탈락
    visited = [0] * N
    perm(N, R, visited, user_id, banned_id, 0, [])

    return len(answer)


print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"]))


#------
# from itertools import permutations
#
#
# def check(user, ban):
#     if len(user) != len(ban):
#         return False
#     else:
#         for i, j in zip(user, ban):
#             if j == '*':
#                 continue
#             if i != j:
#                 return False
#         return True
#
#
# def solution(user_id, banned_id):
#     answer = []
#
#     for i in permutations(user_id, len(banned_id)):
#         count = 0
#         for a, b in zip(i, banned_id):
#             if check(a, b):
#                 count += 1
#
#         if count == len(banned_id):
#             if set(i) not in answer:
#                 answer.append(set(i))
#
#     return len(answer)