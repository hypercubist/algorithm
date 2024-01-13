from collections import deque

def chk(gh):
    green = 0
    for i in range(n):
        for j in range(m):
            if gh[i][j] == 0:
                green += 1
    if green == 0:
        return True #모두 익었을 때
    else:
        return False #안 익은 토마토가 남았을 때

def start_node(gh, start):
    for i in range(n):
        for j in range(m):
            if gh[i][j] == 1:
                start.append((i,j))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
m, n = map(int, input().split())

gh = []
for _ in range(n):
    gh.append(list(map(int, input().split())))

if chk(gh):
    print(0)
else:
    start = []
    start_node(gh, start)
    q = deque(start)
    count = 0
    while True:
        if len(q) == 0:
            count -= 1
            break
        else:
            tempq = []
            while q:
                x, y = q.popleft()
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < n and 0 <= ny < m:
                        if gh[nx][ny] == 0:
                            gh[nx][ny] = 1
                            tempq.append((nx, ny))
            q = deque(tempq)
            count += 1

    if chk(gh):
        print(count)
    else:
        print(-1)