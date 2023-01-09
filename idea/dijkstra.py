# 노드에서 노드 간 최단거리를 구해주는 알고리즘이다.
# 음의 간선이 없을 때 정상적으로 동작, 실제 거리는 모두 양수 이므로 gps의 기본 알고리즘
# 매번 가장 비용이 적은 노드를 선택하는 그리디
# 매 단계 마다 방문하지 않은 노드 중에서 거리가 짧은 노드를 선택하기 위해 1차원 리스트의 모든 원소를 확인(N)
# 매 단계 마다 하나의 노드에 대한 최단거리를 확실히 찾는다.

#간단한 방법
import sys
input = sys.stdin.readline
INF = int(1e9)
n, m = map(int, input().split()) # n = 노드 갯수, m = 간선 갯수
start = int(input()) # 시작노드
graph = [[] for _ in range(n+1)] # 노드 연결 정보 리스트
visited = [False] * (n+1) # 방문 여부 리스트
distance = [INF] * (n+1) # 최단 거리 테이블을 무한대로 초기화
for _ in range(m): # 그래프에 노드 간선 정보 입력
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
#방문하지 않은 노드 중 거리가 가장 짧은 노드
def get_smallest_node():
    min_value = INF
    index = 0 # 가장 거리가 짧은 노드(인덱스)
    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index
def dijkstra(start):
    #시작 노드 초기화
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1] #인접 노드 거리 입력
    #시작 노드 제외한 모든 노드에 대해서 반복
    for i in range(n-1):
        # 현재 가장 거리가 짧은 노드 방문처리
        now = get_smallest_node()
        visited[now] = True
        # 현재 노드와 연결된 노드 확인
        for j in graph[now]:
            cost = distance[now] + j[1] # cost = 현재 노드를 거쳐 연결된 노드로 이동했을 때 거리
            if cost < distance[j[0]]: # 기존 최단거리보다 짧은 경우, 최단거리 갱신
                distance[j[0]] = cost

#개선된 방법
#현재 가장 가까운 노드를 찾기위해 선형시간이 필요 -> 로그 시간만 사용하는 힙 사용
import heapq
def dijkstra2(graph, start, distance):
    # distance : 각 노드의 최단거리를 저장할 배열 distance = [INF] * (n+1)로 초기화 한다.
    q = []
    # 힙에 삽입되는 원소가 배열이라면 첫번째 원소를 기준으로 정렬되므로 (거리, 노드)로 정의해서 넣으면 거리를 기준으로 정렬된다.
    # 시작노드까지의 거리 0으로 초기화
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        # 힙에 저장된 노드 중 최단거리가 최소인 노드 pop
        dist, now = heapq.heappop(q)
        # 이미 최단거리가 갱신되어 힙에서 꺼낸 거리보다 짧은 경우 -> 패스
        if distance[now] < dist:
            continue
        for i in graph[now]: # now와 인접한 노드들을 확인
            cost = dist + i[1] # now를 거쳐서 i[0] 노드로 갈때 거리
            if cost < distance[i[0]]: # 새로 계산된 cost 거리가 기존에 저장된 거리보다 짧은 경우 갱신
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0])) # 갱신된 최단거리 노드를 힙에 삽입


