# Word Search

class Solution:

    def exist(self, board, word):
        dx = [0, 1, 0, -1]
        dy = [-1, 0, 1, 0]
        row, col = len(board), len(board[0])
        vstd = [[False for _ in range(col)] for _ in range(row)]   # 방문한 칸

        word_set = set(word)
        board_set = set([])
        for item in board:
            board_set |= set(item)
        result_set = word_set - board_set

        if len(result_set) > 0:
            return False

        def is_available(x, y):
            return 0 <= x < row and 0 <= y < col

        def bt(x, y, idx):
            if not vstd[x][y] and board[x][y] == word[idx]:
                if idx == len(word)-1:
                    return True
                vstd[x][y] = True
                result = False
                for z in range(4):
                    nx = x + dx[z]
                    ny = y + dy[z]
                    if is_available(nx, ny):
                        if bt(nx, ny, idx+1):
                            result = True
                vstd[x][y] = False
                return result

        for i in range(row):
            for j in range(col):
                if bt(i, j, 0):
                    return True

        return False


