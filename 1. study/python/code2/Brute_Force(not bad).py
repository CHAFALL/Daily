# 패턴이 처음 발생하는 곳 위치 찾기
def BruteForce(pattern, text):
    i = 0
    j = 0
    while i < N and j < M:
        if text[i] != pattern[j]:
            i = i-j
            j = -1
        i += 1
        j += 1
    if j == M:
        return i - M
    else:
        return -1

# 해당 패턴이 몇 개인지 구해보기
def BruteForce2(pattern, text):
    i = 0
    j = 0
    counts = 0

    while i < N and j < M:

        if pattern[j] != text[i]:
            i = i-j
            j = -1

        i+=1
        j+=1

        if j == M:
            counts +=1
            j = 0

    return counts


pattern = "is"
text = "This is a book~!"
M = len(pattern)
N = len(text)

print(BruteForce(pattern, text))
print(BruteForce2(pattern, text))






