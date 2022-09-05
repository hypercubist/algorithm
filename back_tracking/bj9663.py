n = int(input())

visited = [[False]*(n+1) for _ in range(n+1)]

result = 0
dx = []
dy = []
def dfs(x, y, count, visited):
    global n, result
    if count == n:
        result += 1
        return
    if not visited[x][y]:
        #주변방문처리
        for i in range(1, n+1):
            visited[x][i] = True
            visited[i][y] = True
        for

        for i in range(1, n+1):
            for j in range(1, n+1):
                dfs(i, j, count+1, visited)


