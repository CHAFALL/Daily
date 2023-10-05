import sys
sys.stdin = open('D4047.txt')

T = int(input())
for tc in range(1, T+1):
    S = input() # 왜 내가 굳이 처음에 리스트로 받았을까?
    C1 = [0] * 14
    C2 = [0] * 14
    C3 = [0] * 14
    C4 = [0] * 14
    counts1 = 13
    counts2 = 13
    counts3 = 13
    counts4 = 13
    flag = 1
    for i in range(len(S) // 3):
        shape = S[3 * i]
        num = int(S[3 * i + 1 : 3 * i + 3])

        if shape == 'S':
            if C1[num] != 1:
                C1[num] += 1
                counts1 -= 1
            else:
                flag = 0
                break
        elif shape == 'D':
            if C2[num] != 1:
                C2[num] += 1
                counts2 -= 1
            else:
                flag = 0
                break
        elif shape == 'H':
            if C3[num] != 1:
                C3[num] += 1
                counts3 -= 1
            else:
                flag = 0
                break
        elif shape == 'C':
            if C4[num] != 1:
                C4[num] += 1
                counts4 -= 1
            else:
                flag = 0
                break
    if flag == 1:
        print(f'#{tc} {counts1} {counts2} {counts3} {counts4}')
    else:
        print(f'#{tc} ERROR')
