# 2020 KAKAO BLIND RECRUITMENT 블록 이동하기

# 시작점 2개에서 유리한 n, n까지의 최단거리 중 더 짧은 것을 선택

from collections import deque

def solution(board):
    n = len(board)
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]

    def is_valid(x, y):
        return 0 <= x < n and 0 <= y < n and board[x][y] == 0

    def bfs(start):
        visited = [[False] * n for _ in range(n)]
        q = deque([(start[0], start[1], 0)])
        visited[start[0]][start[1]] = True
        while q:
            x, y, d = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if is_valid(nx, ny) and not visited[nx][ny]:
                    if nx == n-1 and ny == n-1:
                        return d+1
                    visited[nx][ny] = True
                    q.append((nx, ny, d+1))

    start_1 = (0, 0)
    start_2 = (0, 1)

    return min(bfs(start_1), bfs(start_2))


print(solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]))