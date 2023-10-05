# def countingsort(arr, n, k):
#     count_table = [0] * (k+1) # 이거 괄호 열어줘야 됨
#     temp = [0] * n
#
#     # 카운팅
#     for i in range(n):
#         count_table[arr[i]] +=1
#     # 누적
#     for i in range(1, k+1): #이거 어디서 부터 시작하냐에 따라 아래에 기입하는 것 달라짐
#         count_table[i] += count_table[i-1]
#     # 자리배치
#     for i in range(n-1, -1, -1):
#         count_table[arr[i]] -= 1
#         temp[count_table[arr[i]]] = arr[i]
#
#     return temp # 새로운 배열로 해야겠지?
#
#
#
# arr = [0, 4, 1, 3, 1, 2, 4, 1]
# n = len(arr)
# k = 4  #(가장 큰 원소)
# print(countingsort(arr, n, k))
#
#

#=========================================================================================
def countingsort(arr, N, k):
    pass


arr = [0, 4, 1, 3, 1, 2, 4, 1]
n = len(arr)
k = 4  #(가장 큰 원소)
print(countingsort(arr, n, k))