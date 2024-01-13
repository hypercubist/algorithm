# 잘라낼 수 있는 모든 경우의 수에 대해서 w로 시작하는 케이스와 b로 시작하는 케이스를 각각 검사한다.

n, m = map(int, input().split())
board = []

for _ in range(n):
    board.append(list(input()))

def counting(x, y): # x, y는 잘라내기 시작하는 지점
    w_count = 0 # [0][0]이 흰색인 케이스
    b_count = 0 # [0][0]이 검정색인 케이스
    count = 0
    for i in range(8):
        for j in range(8):
            if (i+j) % 2 == 0:
                if board[x+i][y+j] == 'W':
                    b_count += 1
                else:
                    w_count += 1
            else:
                if board[x+i][y+j] == 'W':
                    w_count += 1
                else:
                    b_count += 1

    return min(w_count, b_count)

result = 1e9
for i in range(0, n-7):
    for j in range(0, m-7):
        result = min(result, counting(i, j))

print(result)
