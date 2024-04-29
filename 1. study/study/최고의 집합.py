# 최대한 붙어있는 것들로 하는 것이 유리
# 중복이 허용이 됨
def solution(n, s):
    answer = []

    if n > s:
        return [-1]

    # 몫과 나머지
    quotient = s // n
    remainder = s % n

    for _ in range(n):
        answer.append(quotient)


    # 나머지 만큼 추가해주기 (뒤에서부터)
    for i in range(remainder):
        answer[n - 1 - i] = answer[n - 1 - i] + 1

    return answer



print(solution(2, 9))