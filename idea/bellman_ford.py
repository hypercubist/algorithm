# 간선에 집중하는 최단거리 알고리즘
# A -> B 로 이동하는 간선이 있을 때 이 간선을 이용하면 A 또는 B의 최단거리를 갱신할 수 있는지 확인
# 간선의 길이가 양수일 때는 A 또는 B 정점 중 기존 최단거리가 더 긴 정점만 갱신될 가능성이 있다.
# 더 긴 쪽을 들러서와봤자 기존 최단거리보다 오래걸리기 때문
# A, B 정점 중, 긴 쪽의 최단거리 > 짧은 쪽의 최단거리 + A-B간선거리  이면  긴 쪽의 최단거리를 갱신한다.

INF = 1e9
def bellman_ford(graph, n, s): # n = 정점의 갯수 # s = 시작 노드
    dist = [INF] * (n+1) # 먼저 최단거리를 저장할 배열을 만들고 무한대로 초기화한다.
    dist[s] = 0 # 출발점의 최단거리는 0으로 초기화한다.
    changed = True # 간선들을 순회하고 나서 갱신된 최단거리가 있는지 확인하는 플래그
    while changed:
        changed = False
        for e in graph:
            a = e[0]
            b = e[1]
            cost = e[2]
            if dist[b] > dist[a] + cost: # 해당 간선을 이용하는 것이 더 유리하면 갱신한다.
                dist[b] = dist[a] + cost
                changed = True
    return dist

    