import sys
input = sys.stdin.readline

INF = 1e9
n = int(input())
m = int(input())

result = [[INF] * (n+1) for _ in range(n+1)]

for i in range(n+1):
    for j in range(n+1):
        if i == j:
            result[i][j] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    result[a][b] = min(result[a][b], c)
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            result[i][j] = min(result[i][j], result[i][k] + result[k][j])

for i in range(1, n+1):
    for j in range(1, n+1):
        if result[i][j] >= INF:
            print(0, end=" ")
        else:
            print(result[i][j], end=" ")
    print()
