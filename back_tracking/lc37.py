# 37.sudoku

class Solution:
    def solveSudoku(self, board):

        def possible_list(board, i, j):
            result = [x for x in range(1, 10)]
            
            # 불가한 숫자 빼기
            # 가로
            for k in range(9):
                result.remove(board[i][k])
            
            # 세로
            for k in range(9):
                result.remove(board[k][j])

            # 주변
            i_mok = i // 3
            j_mok = j // 3
            for x in range(i_mok * 3, (i_mok+1) * 3):
                for y in range(j_mok * 3, (j_mok+1) * 3):
                    result.remove(board[x][y])


            return result