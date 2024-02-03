# 2020 KAKAO BLIND RECRUITMENT 블록 이동하기

# 이동했을 때의 좌표 변화를 정의
# 좌표 2개의 이동을 정의
# 이동 시 가능한 상황인지 제한사항을 확인
# 이동 후 방문 처리 시 두 좌표를 기록, 기록 시 두 좌표의 앞뒤가 바뀔 수 있으므로 두 케이스 모두 저장
# 이동 횟수를 카운트

from collections import deque


def solution(board):
    n = len(board)

    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]

    def is_valid(x, y):
        return 0 <= x < n and 0 <= y < n and board[x][y] == 0

    # 현재 좌표에서 이동 가능한 위치를 리스트로 리턴
    def possible_move_case(x1, y1, x2, y2):
        result = []
        # 동서남북 한 칸씩 이동
        for i in range(4):
            nx1 = x1 + dx[i]
            ny1 = y1 + dy[i]
            nx2 = x2 + dx[i]
            ny2 = y2 + dy[i]
            if is_valid(nx1, ny1) and is_valid(nx2, ny2):
                result.append((nx1, ny1, nx2, ny2))

        # 회전(가로 -> 세로)
        if x1 == x2:
            # up
            if is_valid(x1+1, y1) and is_valid(x2+1, y2):
                result.append((x1, y1, x1+1, y1))
                result.append((x2, y2, x2+1, y2))
            # down
            elif is_valid(x1-1, y1) and is_valid(x2-1, y2):
                result.append((x1, y1, x1-1, y1))
                result.append((x2, y2, x2-1, y2))
        # 회전(세로 -> 가로)
        elif y1 == y2:
            # left
            if is_valid(x1, y1-1) and is_valid(x2, y2-1):
                result.append((x1, y1, x1, y1-1))
                result.append((x2, y2, x2, y2-1))
            # right
            elif is_valid(x1, y1+1) and is_valid(x2, y2+1):
                result.append((x1, y1, x1, y1+1))
                result.append((x2, y2, x2, y2+1))
        return result

    def bfs(x1, y1, x2, y2):
        visited = []
        q = deque([(x1, y1, x2, y2, 0)])
        #두 좌표의 앞뒤가 바뀔 수 있으므로 두 케이스 모두 저장
        visited.append((x1, y1, x2, y2))
        visited.append((x2, y2, x1, y1))
        while q:
            xx1, yy1, xx2, yy2, c = q.popleft()
            if (xx1 == n-1 and yy1 == n-1) or (xx2 == n-1 and yy2 == n-1):
                return c
            move_case = possible_move_case(xx1, yy1, xx2, yy2)
            for case in move_case:
                if case not in visited:
                    xxx1, yyy1, xxx2, yyy2 = case
                    q.append((xxx1, yyy1, xxx2, yyy2, c+1))
                    visited.append((xxx1, yyy1, xxx2, yyy2))
                    visited.append((xxx2, yyy2, xxx1, yyy1))

    return bfs(0, 0, 0, 1)


print(solution(
    [[0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 1, 1, 0, 0], [0, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 1, 1, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 0]]
))