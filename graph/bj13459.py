# 구슬탈출

# 구슬 2개의 상태를 보관(방문)하는 것이 핵심

from collections import deque
n, m = map(int, input().split())

gh = []
for _ in range(n):
    gh.append(input())
print(gh)
# R, B, O 위치 확인
pr = (0, 0)
pb = (0, 0)
po = (0, 0)
for i in range(n):
    for j in range(m):
        if gh[i][j] == 'R':
            pr = (i, j)
        elif gh[i][j] == 'B':
            pb = (i, j)
        elif gh[i][j] == 'O':
            po = (i, j)

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
def next_coord(x, y, idx):
    while True:

        nx = x + dx[idx]
        ny = y + dy[idx]
        if gh[nx][ny] == '#':
            return (x, y)
        elif gh[nx][ny] == 'O':
            return (nx, ny)
        else:
            x = nx
            y = ny

def coord_correction(coord_r, coord_b, coord_nr, coord_nb): #좌표 보정
    cor_r = [coord_nr[0], coord_nr[1]]
    cor_b = [coord_nb[0], coord_nb[1]]
    if coord_r[0] == coord_b[0]: # row가 같은 경우 -> col비교
        if coord_r[1] < coord_b[1]:
            if coord_r[1] < coord_nr[1]:
                cor_r[1] -= 1
            else:
                cor_b[1] += 1
        else:
            if coord_r[1] < coord_nr[1]:
                cor_b[1] -= 1
            else:
                cor_r[1] += 1
    elif coord_r[1] == coord_b[1]: # col이 같은 경우 -> row비교
        if coord_r[0] < coord_b[0]:
            if coord_r[0] < coord_nr[0]:
                cor_r[0] -= 1
            else:
                cor_b[0] += 1
        else:
            if coord_r[0] < coord_nr[0]:
                cor_b[0] -= 1
            else:
                cor_r[0] += 1

    return cor_r, cor_b

def bfs(start_r, start_b):
    count = 1e9
    visited = [(start_r, start_b)]
    q = deque([(start_r, start_b, 0)])
    while q:
        r, b, c = q.popleft()
        for i in range(4):
            nr = next_coord(r[0], r[1], i)
            nb = next_coord(b[0], b[1], i)
            if nr == nb == po: # 둘 다 탈출한 경우
                continue
            elif nr == po:
                count = min(count, c)
            elif nb == po:
                continue
            else:
                if nr == nb:
                    nr, nb = coord_correction(r, b, nr, nb)
                if (nr, nb) not in visited:
                    visited.append((nr, nb))
                    q.append((nr, nb, c+1))
    return count

if bfs(pr, pb) <= 10:
    print(1)
else:
    print(0)



