# 스타트 택시

# 최단거리 > bfs
# 같은 거리에 승객이 있는 경우 행번호 > 열번호 순서

from collections import deque
# n=공간 변의 길이, m=승객 수, f=연료량
n, m, f = map(int, input().split())
# gh=공간, 0=빈칸, 1=벽
gh = []
for _ in range(n):
    gh.append(list(map(int, input().split())))
# st=시작 위치
sx, sy = map(int, input().split())
now = (sx-1, sy-1) # 인덱스 조정 -1
# psngr=승객위치, des=목적지, 인덱스로 연결
psngr, dest = [], []
for i in range(m):
    a, b, c, d = map(int, input().split())
    psngr.append((a-1, b-1, i))
    dest.append((c-1, d-1, i)) #인덱스 조정 -1

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
def is_valid(x, y): # 이동 가능 검증
    return 0 <= x < n and 0 <= y < n and gh[x][y] == 0
def find_close_destination(start, destinations):
    # 현재위치 확인
    for a, b, i in destinations:
        if start[0] == a and start[1] == b:
            return 0, a, b, i

    possible_dest = [] # 가장 가까운 곳 중 선순위를 확인하기 위한 배열
    visited = [[False] * n for _ in range(n)]
    visited[start[0]][start[1]] = True
    q = deque([(start[0], start[1], 0)]) # 좌표와 거리 파라미터 전달
    while q:
        x, y, d = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if is_valid(nx, ny) and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny, d+1))
                for dest_x, dest_y, k in destinations: # 현재 이동가능한 위치 중 목적지가 있는지 확인
                    if nx == dest_x and ny == dest_y:
                        possible_dest.append((d+1, nx, ny, k)) # 최단거리 목적지 배열에 추가
    if len(possible_dest) > 0:
        possible_dest.sort() # 최단거리 목적지 중 선순위 정렬(행, 열 순서)
        return possible_dest[0][0], possible_dest[0][1], possible_dest[0][2], possible_dest[0][3]
    else:
        return -1, -1, -1, -1 # 이동이 불가한 경우

while len(dest) > 0:
    # 현재 위치에서 가장 가까운 승객 위치 찾기
    dist_p, pa, pb, pi = find_close_destination(now, psngr)

    if dist_p == -1:
        break

    # 이동
    now = (pa, pb)
    f -= dist_p
    if f < 0:
        break
    # 승객 목적지 거리 확인
    target_dest = []
    for i in range(len(psngr)):
        if pa == psngr[i][0] and pb == psngr[i][1]:
            target_dest.append((dest[i][0], dest[i][1], dest[i][2]))

    dist_d, da, db, di  = find_close_destination(now, target_dest)

    if dist_d == -1:
        break

    now = (da, db)
    f -= dist_d

    if f < 0:
        break

    f += dist_d * 2

    psngr.remove((pa, pb, pi))
    dest.remove((da, db, di))

if len(dest) > 0:
    print(-1)
else:
    print(f)