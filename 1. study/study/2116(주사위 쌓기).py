# N = int(input()) # 주사위의 갯수
# arr = [list(map(int, input().split())) for _ in range(N)]
#
# # A - F, B - D, C - E (속박 되는 것)
# # 1 - 6, 2 - 4, 3 - 5
# # 0 - 5, 1 - 3, 2 - 4
# # 1번의 윗면 숫자가 1일 때부터 6일 때로 for문 돌리고
# # 맨 위도 종속이 되네 음... 오히려 좋아
# # 맨 밑에놈은 내가 강제로 제한을 둘꺼니깐.
#
# # 남은 4개 중에서 젤 큰거로 max 구하면 됨.
#
#
# # 같이 못 쓰게 될 놈 찾기
# def find(i, j):
#     findNum = -1
#     if j == 0:
#         findNum = arr[i][5]
#     elif j == 1:
#         findNum = arr[i][3]
#     elif j == 2:
#         findNum = arr[i][4]
#     elif j == 3:
#         findNum = arr[i][1]
#     elif j == 4:
#         findNum = arr[i][2]
#     elif j == 5:
#         findNum = arr[i][0]
#
#     return findNum
#
#
#
# # 1번의 윗면 숫자가 i(1~6)일 경우 무엇이 속박 되니? (옆 면이 될 수 없는 2개가 뭐니!)
# for num in range(1, 7):
#     for i in range(N):
#         for j in range(6):
#             if arr[i][j] == num:
#                 findNum = find(i, j)
#
#--------------------------


# A - F, B - D, C - E (속박 되는 것)
# 1 - 6, 2 - 4, 3 - 5
# 0 - 5, 1 - 3, 2 - 4
# 1번의 윗면 숫자가 1일 때부터 6일 때로 for문 돌리고
# 맨 위도 종속이 되네 음... 오히려 좋아
# 맨 밑에놈은 내가 강제로 제한을 둘꺼니깐.

# 남은 4개 중에서 젤 큰거로 max 구하면 됨.

# 같이 못 쓰게 될 놈 찾고 배열에서 같이 배제 시키기
# def find(i, j):
#     dice = [1, 2, 3, 4, 5, 6]
#     dice.remove(num)
#     if j == 0:
#         dice.remove(arr[i][5])
#     elif j == 1:
#         dice.remove(arr[i][3])
#     elif j == 2:
#         dice.remove(arr[i][4])
#     elif j == 3:
#         dice.remove(arr[i][1])
#     elif j == 4:
#         dice.remove(arr[i][2])
#     elif j == 5:
#         dice.remove(arr[i][0])
#
#     return max(dice)
#
#
# N = int(input())  # 주사위의 갯수
# arr = [list(map(int, input().split())) for _ in range(N)]
# # 1번의 윗면 숫자가 i(1~6)일 경우 무엇이 속박 되니? (옆 면이 될 수 없는 2개가 뭐니!)
# max_value = 0
# for num in range(1, 7):
#     max_temp = 0
#     for i in range(N):
#         for j in range(6):
#             if arr[i][j] == num:
#                 temp = find(i, j)
#                 max_temp += temp
#
#     max_value = max(max_value, max_temp)
#
# print(max_value)

#-----------

import sys
limit_number = 15000
sys.setrecursionlimit(limit_number)

# 숫자를 통해서 인덱스 값 찾기(웹을 해서 그런가 이거 밖에 생각 안남)
def find_index(num, v):
    if v == N:  # 인덱스 오류 방지
        return
    for i in range(6):
        if arr[v][i] == num:
            return i

def find(index, v): #현재 주사위의 아랫면 인덱스, 주사위 깊이
    global total
    if v == N:
        return

    dice = [1, 2, 3, 4, 5, 6]
    # 아랫면 숫자 제거
    dice.remove(arr[v][index])
    # 윗면 숫자 제거
    dice.remove(arr[v][face[index]])

    total += max(dice)
    # 다음 주사위에 지장을 줄 윗면 숫자의 인덱스 찾기
    n_index = find_index(arr[v][face[index]], v + 1)
    find(n_index, v + 1)

    return

face = {
    0: 5,
    1: 3,
    2: 4,
    3: 1,
    4: 2,
    5: 0
}

N = int(input())  # 주사위의 갯수
arr = [list(map(int, input().split())) for _ in range(N)]

max_value = 0

for index in range(0, 6):
    total = 0
    find(index, 0)  # 주사위의 옆면 숫자들 찾기
    max_value = max(max_value, total)

print(max_value)