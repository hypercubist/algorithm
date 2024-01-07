# 37.sudoku
import copy


class Solution:
    def solveSudoku(self, board):
        output = ""
        def possible_list(board, i, j):
            result = [str(x) for x in range(1, 10)]
            
            # 불가한 숫자 빼기
            # 가로
            for k in range(9):
                if board[i][k] in result:
                    result.remove(board[i][k])
            
            # 세로
            for k in range(9):
                if board[k][j] in result:
                    result.remove(board[k][j])

            # 주변
            i_mok = i // 3
            j_mok = j // 3
            for x in range(i_mok * 3, (i_mok+1) * 3):
                for y in range(j_mok * 3, (j_mok+1) * 3):
                    if board[x][y] in result:
                        result.remove(board[x][y])

            return result


        def bt(x, y, output):
            if x == 9 and y == 9:
                output = copy.deepcopy(board)
            for i in range(9):
                for j in range(9):
                    if board[i][j] == ".":
                        for num in possible_list(board, i, j):
                            board[i][j] = num
                            bt(i, j, output)
                            board[i][j] = "."


        bt(0, 0, output)