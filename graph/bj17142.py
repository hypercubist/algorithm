# 연구소3

# 비활성바이러스 중 활성시킬 바이러스를 고른다(조합)
# 활성바이러스를 확산시키면서 걸린 시간을 구한다.(bfs)
# 활성바이러스가 비활성바이러스에 도착한 경우 활성된다(비활성바이러스는 빈 칸과 동일하다고 볼 수 있다)
# 바이러스 확산이 끝났을 때 빈 공간이 있는지 확인한다.

from itertools import combinations
from collections import deque
import copy

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

def chk_time(gh): # 전체 감염에 걸린 시간 확인
    max_time = 0
    for i in range(n):
        for j in range(n):
            if gh[i][j] == 0:
                return 1e9
            # 경과시간은 음수로 기록했으므로 음수에서만 확인, 원래 바이러스가 있던 위치는 depth가 덮어쓰더라도 카운팅하지 않음
            elif gh[i][j] < 0 and graph[i][j] != 2:
                max_time = max(max_time, -gh[i][j]) # 음수 -> 양수로 변환
    return max_time

def valid(gh, x, y): # 이동 적합성 검사
    return 0 <= x < n and 0 <= y < n and (gh[x][y] == 0 or gh[x][y] == 2)

def bfs(gh, start):

    q = deque([(x, y, 0) for x, y in start])
    while q:
        x, y, depth = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if valid(gh, nx, ny):
                q.append((nx, ny, depth-1))
                gh[nx][ny] = depth - 1

virus = [] # 바이러스 위치(bfs 시작 위치 확인)
for i in range(n):
    for j in range(n):
        if graph[i][j] == 2:
            virus.append((i, j))

active_virus_combi = combinations(virus, m) # 활성 바이러스 선택 조합
min_time = 1e9
for active_virus in active_virus_combi:
    for v in active_virus:
        graph[v[0]][v[1]] = 3 # 활성 바이러스 놓기(활성바이러스 = 3 표시)

    graph_case = copy.deepcopy(graph) # 활성 바이러스 놓은 상태의 그래프 복사
    bfs(graph_case, active_virus) # 바이러스 확산
    min_time = min(min_time, chk_time(graph_case)) # 걸린 시간 확인

    for v in active_virus:
        graph[v[0]][v[1]] = 2 # 활성 바이러스 제거, 복사할 그래프는 원본 유지해야하므로

if min_time == 1e9:
    print(-1)
else:
    print(min_time)

