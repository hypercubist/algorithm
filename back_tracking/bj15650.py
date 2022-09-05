from itertools import combinations as c

n, m = map(int, input().split())
arr = [x for x in range(1, n+1)]

result = list(c(arr, m))

for i in range(len(result)):
    for j in range(m):
        print(result[i][j], end=" ")
    print()