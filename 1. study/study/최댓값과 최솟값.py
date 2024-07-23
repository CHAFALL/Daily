def solution(s):
    list_s = list(map(int, s.split(' ')))
    list_s.sort() # 오름차순 정렬

    return str(list_s[0]) + " " + str(list_s[-1])

print(solution("-1 -2 -3 -4"))