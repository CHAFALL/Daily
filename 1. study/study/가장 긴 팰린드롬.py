# 짝수일 경우와 홀수일 경우를 고려해줘야 됨.

from enum import Enum

class Type(Enum):
    EVEN = 1
    ODD = 2

def maxLength(s, left, right, type):

    N = len(s)
    while left >= 0 and right < N:
        if s[left] == s[right]:
            left -= 1
            right += 1
        else:
            break

    return right - left - 1


def solution(s):
    answer = 0

    N = len(s)

    # 즉시 종료 조건
    if N == 1 or s == s[::-1]:
        return N

    for i in range(N - 1):
        # 짝수일 때, 홀수일 때 모두 고려하기
        answer = max(answer, maxLength(s, i, i + 1, Type.EVEN), maxLength(s, i, i + 2, Type.ODD))


    return answer

print(solution("abacde"))