# dfs는 stack과 관련이 있다.


#재귀로 구현한 dfs, 방문 내역을 기록
def dfs(graph, v, visited):
    #graph : 노드 연결 정보가 기록된 리스트(인접리스트)
    #v(vertex) : 탐색할 노드
    #visited : 방문 기록 [False] * n 으로 초기화
    visited[v] = True #노드 방문
    print(v, end=' ')
    for i in graph[v]: # 현재 노드와 연결된 노드 i 중에서
        if not visited[i]: # 아직 방문하지 않은 노드를
            dfs(graph, i, visited) # 재귀적으로 방문,  graph, visited는 외부에 선언되어 있고 참조하여 업데이트한다.

