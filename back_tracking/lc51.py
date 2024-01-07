#N-Queens


class Solution:
    def solveNQueens(self, n: int):
        output = []
        default_board = [["." for _ in range(n)] for _ in range(n)]

        set_j = set([])
        set_p = set([])
        set_m = set([])

        def is_possible(x, y):
            if y in set_j:
                return False
            if x+y in set_p:
                return False
            if x-y in set_m:
                return False
            return True

        def bt(i):
            if i == n:
                result = []
                for item in default_board:
                    row = "".join(item)
                    result.append(row)
                output.append(result)
            for j in range(n):
                if is_possible(i, j):
                    default_board[i][j] = "Q"
                    set_j.add(j)
                    set_p.add(i+j)
                    set_m.add(i-j)
                    bt(i+1)
                    default_board[i][j] = "."
                    set_j.remove(j)
                    set_p.remove(i+j)
                    set_m.remove(i-j)

        bt(0)
        return output

