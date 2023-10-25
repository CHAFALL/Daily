import sys
sys.stdin = open('D11750.txt')

# hex_to_bin = {
#     '0': '0000',
#     '1': '0001',
#     '2': '0010',
#     '3': '0011',
#     '4': '0100',
#     '5': '0101',
#     '6': '0110',
#     '7': '0111',
#     '8': '1000',
#     '9': '1001',
#     'A': '1010',
#     'B': '1011',
#     'C': '1100',
#     'D': '1101',
#     'E': '1110',
#     'F': '1111'
# }
# T = int(input())
# for tc in range(1, T+1):
#     N, number = input().split()
#     N = int(N)
#     bin = ''
#     for i in range(N):
#         bin += hex_to_bin[number[i]]
#     print(f'#{tc} {bin}')
#----------------------------------------------------------------
# 딕셔너리 안 쓰고 가능?

# 매핑 테이블
hex_bin = [
    [0,0,0,0],
    [0,0,0,1],
    [0,0,1,0],
    [0,0,1,1],
    [0,1,0,0],
    [0,1,0,1],
    [0,1,1,0],
    [0,1,1,1],
    [1,0,0,0],
    [1,0,0,1],
    [1,0,1,0],
    [1,0,1,1],
    [1,1,0,0],
    [1,1,0,1],
    [1,1,1,0],
    [1,1,1,1]
]

def a_to_dec(c): # 16진수 -> 10진수
    if c <= '9':
        return ord(c) - ord('0')
    else:
        return ord(c) - ord('A') + 10

def make_bin(x): # 10진수 -> 2진수
    for i in range(4):
        ans .append(hex_bin[x][i])

T = int(input())
for tc in range(1, T+1):
    N, hex = input().split()
    N = int(N)

    ans = []
    for i in range(N):
        make_bin(a_to_dec(hex[i]))

    print(f"#{tc} {''.join(map(str, ans))}")
