# 연구소

# 퍼진다? > bfs

# 벽 3개를 임의의 위치에 놓는다
# 벽 3개를 놓은 상황에서 바이러스를 확산시킨다(bfs)
# 감염되지 않은 공간의 크기를 구한다
# 구한 공간의 크기 중 가장 큰 것을 찾는다.
from itertools import combinations
from collections import deque
import copy

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

def count_clean(gh):
    count = 0
    for i in range(n):
        for j in range(m):
            if gh[i][j] == 0:
                count += 1
    return count

def valid(gh, x, y):
    return 0 <= x < n and 0 < y <= m and gh[x][y] == 0
def bfs(gh, start):
    q = deque(start)
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if valid(gh, x, y):
                q.append((nx, ny))
                gh[nx][ny] = 2

answer = 0
wall = 0
space = []
virus = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            space.append((i, j))
        elif graph[i][j] == 2:
            virus.append((i, j))

space_combi = combinations(space, 3)

for spaces in space_combi:
    for space in spaces:
        graph[space[0]][space[1]] = 1

    # do
    graph_case = copy.deepcopy(graph)
    bfs(graph_case, virus)
    answer = max(answer, count_clean(graph_case))

    for space in spaces:
        graph[space[0]][space[1]] = 0

print(answer)

