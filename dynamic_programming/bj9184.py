import sys
input = sys.stdin.readline

board = [[[None for _ in range(21)] for _ in range(21)] for _ in range(21)]
board[0][0][0] = 1

def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    elif a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)
    else:
        if board[a][b][c] is not None:
            return board[a][b][c]
        else:
            if a < b < c:
                board[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
            else:
                board[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
            return board[a][b][c]


while True:
    a, b, c = map(int, input().split())
    if a==-1 and b==-1 and c==-1:
        break
    else:
        result = w(a, b, c)
        print("w("+str(a)+", "+str(b)+", "+str(c)+") = " + str(result))



