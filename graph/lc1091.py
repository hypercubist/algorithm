# Shortest Path in Binary Matrix

# bfs?
# depth 구하기


from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid):
        n = len(grid)

        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1

        def is_inside(x, y):
            return 0 <= x, y < n and grid[x][y] == 0

        q = deque([])
        visited = [[False] * n for _ in range(n)]
        dx = [0, 1, 0, -1, 1, 1, -1, -1]
        dy = [-1, 0, 1, 0, 1, -1, 1, -1]

        visited[0][0] = True
        q.append((0, 0))
        while q:
            x, y = q.popleft()
            for i in range(8):
                nx = x + dx
                ny = y + dy
                if is_inside(nx, ny) and not visited[nx][ny]:
                    q.append((nx, ny))
