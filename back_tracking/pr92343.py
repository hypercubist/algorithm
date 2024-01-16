# 2022 KAKAO BLIND RECRUITMENT 양과 늑대


def solution(info, edges):
    answer = 0
    n = len(info) # 노드의 갯수

    # 간선리스트를 인접리스트로 변환
    graph = [[] for _ in range(n)]
    for edge in edges:
        p, c = edge
        graph[p].append(c)

    sheep = 0
    wolf = 0
    visited = [False] * n







    return answer