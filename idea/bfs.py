# bfs는 queue와 관련이 있다.

# queue로 구현한 bfs, 방문 내역을 기록
from collections import deque
def bfs(graph, s, visited):
    #graph : 노드 연결 정보가 기록된 리스트(인접리스트)
    #s(start) : 시작 노드
    #visited : 방문 기록 [False] * n 으로 초기화
    queue = deque([start]) # 큐에 시작 노드 삽입
    visited[s] = True #시작 노드 방문
    while queue: #queue가 빈 경우 모든 방문 가능한 노드를 방문했다는 뜻
        v = queue.popleft() #queue에서 탐색할 노드 하나를 뽑는다
        print(v, end=' ')
        for i in graph[v]: #현재 탐색 중인 노드의 인접 노드 i 중에서
            if not visited[i]: #아직 방문하지 않은 노드를
                queue.append(i) # queue에 추가하고
                visited[i] = True # 방문 처리한다. queue안에 있는 원소는 이미 방문하였으나 아직 인접 노드는 파악하지 않은 상태이다.


