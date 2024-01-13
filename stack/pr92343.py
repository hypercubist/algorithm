# 2022 KAKAO BLIND RECRUITMENT 양과 늑대

# dfs? bfs? stack?
# 모든 길을 방문하려고 하되 스택을 확인해서 가능 여부를 판단?

from collections import deque

def solution(info, edges):
    answer = 0

    new_edges = [[] for _ in range(len(info))]
    for a, b in edges:
        new_edges[a].append(b)

    path_queue = deque([0])
    safe_count = 0
    sheep_count = 0
    visited = [False] * len(info)

    while path_queue:
        v = path_queue.popleft()
        if info[v] == 0:
            visited[v] = True
            safe_count += 1
            sheep_count += 1
            path_queue.extend(new_edges[v])
        else:
            if safe_count > 1:
                visited[v] = True
                safe_count -= 1
                path_queue.extend(new_edges[v])
            else:
                path_queue.append(v)












    return answer