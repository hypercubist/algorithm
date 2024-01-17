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

def count_clean(gh): # 안전영역 크기 구하기
    count = 0
    for i in range(n):
        for j in range(m):
            if gh[i][j] == 0:
                count += 1
    return count

def valid(gh, x, y): # 이동 적합성 검사
    return 0 <= x < n and 0 <= y < m and gh[x][y] == 0

def bfs(gh, start):
    q = deque(start)
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if valid(gh, nx, ny):
                q.append((nx, ny))
                gh[nx][ny] = 2

wall = 0
space = [] # 빈 공간 확인(벽 놓을 공간 조합하기 위함)
virus = [] # 바이러스 위치(bfs 시작 위치 확인)
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            space.append((i, j))
        elif graph[i][j] == 2:
            virus.append((i, j))

space_combi = combinations(space, 3) # 벽 놓을 공간 조합
answer = 0
for spaces in space_combi:
    for space in spaces:
        graph[space[0]][space[1]] = 1 # 벽 놓기

    graph_case = copy.deepcopy(graph) # 벽 놓은 상태의 그래프 복사
    bfs(graph_case, virus) # 바이러스 확산
    answer = max(answer, count_clean(graph_case)) # 안전영역 크기 구해서 최대값 저장

    for space in spaces:
        graph[space[0]][space[1]] = 0 # 벽 제거, 복사할 그래프는 원본 유지해야하므로

print(answer)

