N = 3
arr = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
#1
for i in range(N):
    for j in range(N):
        if i > j:
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]

for ar in arr:
    print(*ar)

#2

for i in range(N):
    for j in range(i+1, N):
        arr[i][j], arr[j][i] = arr[j][i], arr[i][j]

for ar in arr:
    print(*ar)

#3
# print(*arr) #[1, 2, 3] [4, 5, 6] [7, 8, 9] 속에 있는 것만 꺼내는 느낌인 듯
new_arr = list(zip(*arr))
for new_ar in new_arr:
    print(*new_ar)



