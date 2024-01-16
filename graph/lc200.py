#

# 좌표계를 순회하면서 육지를 찾고(섬 count++) 찾은 곳 주변의 육지를 모두 탐색해서 방문처리한다.
# 이어서 순회하면서 남은 육지도 같은 방식으로 모두 찾는다.
# 방문처리, 섬 카운팅, 주변 탐색 이동이 관건


from collections import deque

class Solution:
    def numIslands(self, grid):
        m = len(grid)
        n = len(grid[0])
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]
        visited = [[False] * n for _ in range(m)]
        count = 0
        q = deque([])
        def is_ok(x, y):
            return 0 <= x < m and 0 <= y < n and grid[x][y] == "1"


        for i in range(m):
            for j in range(n):
                if not visited[i][j] and grid[i][j] == "1":
                    visited[i][j] = True
                    count += 1
                    q.append((i, j))
                    while q:
                        x, y = q.popleft()
                        for k in range(4):
                            nx = x + dx[k]
                            ny = y + dy[k]
                            if is_ok(nx, ny) and not visited[nx][ny]:
                                q.append((nx, ny))
                                visited[nx][ny] = True


        return count


