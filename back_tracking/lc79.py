# 좌표, 백트래킹

def exist(self, board, word):
    result = False
    row = len(board)
    col = len(board[0])
    dx = [0, 1, 0 , -1]
    dy = [1, 0, -1, 0]
    def is_inside(x, y):
        if 0<=x<row and 0<=y<col:
            return True
        else:
            return False

    def bt(x, y, z, flag):
        memory = board[x][y]
        board[x][y] = '.'
        if board[x][y] == word[z]:
            if z == len(word)-1:
                result = True
            else:
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if is_inside(nx, ny) and board[nx][ny] != '.': #이동
                        bt(nx, ny, z+1)
        board[x][y] = memory
        return

    for i in range(row):
        for j in range(col):
            # 선택
            bt(i, j, 0)

    return result