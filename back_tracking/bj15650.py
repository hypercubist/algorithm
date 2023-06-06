# 조합 라이브러리를 이용한 방법
# from itertools import combinations as c
#
# n, m = map(int, input().split())
# arr = [x for x in range(1, n+1)]
#
# result = list(c(arr, m))
#
# for i in range(len(result)):
#     for j in range(m):
#         print(result[i][j], end=" ")
#     print()

# 백트래킹을 이용한 방법
import copy
n, m = map(int, input().split())
arr = [x for x in range(1, n+1)]
result = []
def bt(piece, depth):
    if depth == m:
        result.append(copy.deepcopy(piece))
    else:
        if len(piece) == 0:
            for i in arr:
                piece.append(i)
                bt(copy.deepcopy(piece), depth + 1)
                piece.pop()
        else:
            for i in arr:
                if i > piece[-1]:
                    piece.append(i)
                    bt(copy.deepcopy(piece), depth + 1)
                    piece.pop()


a = []
bt(a, 0)
print(result)