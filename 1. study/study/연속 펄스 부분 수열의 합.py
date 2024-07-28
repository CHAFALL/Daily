def max_subsequence_sum(sequence):
    max_sum = 0
    tmp = 0
    for s in sequence:
        tmp += s
        if tmp < 0:
            tmp = 0
        max_sum = max(max_sum, tmp)
    return max_sum

def solution(sequence):
    sequence2 = sequence[:] # 복사
    N = len(sequence)

    # 전체에 펄스 수열 곱해주기.
    for i in range(N):
        sequence[i] *= (-1) ** (i + 1)
        sequence2[i] *= (-1) ** (i + 2)

    return max(max_subsequence_sum(sequence), max_subsequence_sum(sequence2))

print(solution([2, 3, -6, 1, 3, -1, 2, 4]))




