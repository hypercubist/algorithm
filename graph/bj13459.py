# 구슬탈출

# 구슬 2개의 상태를 보관(방문)하는 것이 핵심

from collections import deque
n, m = map(int, input().split())

gh = []
for _ in range(n):
    gh.append(input())
# R, B, O 위치 확인

prx, pry = (0, 0)
pbx, pby = (0, 0)
for i in range(n):
    for j in range(m):
        if gh[i][j] == 'R':
            prx, pry = (i, j)
        elif gh[i][j] == 'B':
            pbx, pby = (i, j)

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
def next_coord(x, y, idx):
    dist = 0
    while True:
        dist += 1
        x += dx[idx]
        y += dy[idx]
        if gh[x][y] == '#':
            return x-dx[idx], y-dy[idx], dist-1 # 벽 앞에서 멈추기
        elif gh[x][y] == 'O':
            return x, y, dist # 이동 거리도 함께 리턴

def coord_correction(rx, ry, rd, bx, by, bd, idx): #좌표 보정
    if rd < bd: # 더 많이 이동한 구슬이 더 늦게 도착한다.
        bx -= dx[idx]
        by -= dy[idx]
    else:
        rx -= dx[idx]
        ry -= dy[idx]
    return rx, ry, bx, by


def bfs(start_rx, start_ry, start_bx, start_by):
    result = False
    visited = [(start_rx, start_ry, start_bx, start_by)]
    q = deque([(start_rx, start_ry, start_bx, start_by, 0)])
    while q:
        rx, ry, bx, by, c = q.popleft()
        if c >= 10: # 카운트(c)가 10과 같아지면 다음 이동의 카운트는 11이므로 모두 실패이다.
            break
        for k in range(4):
            nrx, nry, nrd = next_coord(rx, ry, k)
            nbx, nby, nbd = next_coord(bx, by, k)
            if gh[nbx][nby] == 'O': # 어쨌든 파랑이 탈출하면 실패
                continue
            if (nrx, nry, nbx, nby) in visited:
                continue
            if gh[nrx][nry] == 'O': # 파랑이 탈출하는 케이스를 제외하고 빨강이 탈출하면 성공
                result = True
                break
            if nrx == nbx and nry == nby:
                nrx, nry, nbx, nby = coord_correction(nrx, nry, nrd, nbx, nby, nbd, k)
            visited.append((nrx, nry, nbx, nby))
            q.append((nrx, nry, nbx, nby, c+1))
        if result:
            break
    return result


if bfs(prx, pry, pbx, pby):
    print(1)
else:
    print(0)



