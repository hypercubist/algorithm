# 2021 카카오 채용연계형 인턴십 거리두기 확인하기

# 맨해튼 거리 > bfs
# 거리 2이내에 사람이 없으면 됨
# 파티션을 제외하고 bfs실행하여 거리 2이내일 때 사람 체크

from collections import deque
def solution(places):

    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    def is_valid(x, y):
        return 0 <= x < 5 and 0 <= y < 5

    def safe(a, b, graph): # 사람이 있는 위치에서 실행하여 주변이 안전한지 확인(거리 2이내에 사람확인)
        visited = [[False] * 5 for _ in range(5)]
        q = deque([(a, b, 0)])
        visited[a][b] = True
        while q:
            x, y, depth = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                # 방 범위 내, 방문하지 않은, 파티션이 아닌 곳 방문
                if is_valid(nx, ny) and not visited[nx][ny] and graph[nx][ny] != 'X':
                    if depth < 2: # 거리가 2이내일 때는 사람이 있는지 확인
                        if graph[nx][ny] == 'P': # 사람 있으면 거리두기 실패
                            return False
                        else: # 사람 없으면 이어서 탐색
                            visited[nx][ny] = True
                            q.append((nx, ny, depth+1))
        return True

    answer = []

    for place in places:
        safe_flag = True
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    if not safe(i, j, place):
                        safe_flag = False
                        break
            if not safe_flag:
                break
        if safe_flag:
            answer.append(1)
        else:
            answer.append(0)

    return answer