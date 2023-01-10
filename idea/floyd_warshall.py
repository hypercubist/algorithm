# 점화식 D(a->b) = min(D(a->b), D(a->k)+D(k->b))
# 시간복잡도 O(N^3)

INF = int(1e9)
n = int(input()) #노드 갯수
m = int(input()) #간선 갯수
# (n+1)*(n+1) 2차원 리스트, 최단 거리를 저장할 것이므로 값을 무한으로 초기화
graph = [[INF] * (n+1) for _ in range(n+1)]

# 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

# 간선 정보 초기화
for _ in range(m):
    a, b, c = map(int, input().split())
    # a에서 b로 가는 비용 c
    graph[a][b] = c

# 플로이드 워셜 알고리즘 수행
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 결과 출력
for a in range(1, n+1):
    for b in range(1, n+1):
        # 해당 노드에 도달할 수 없는 경우 값이 갱신되지 않아 INF로 남아있다.
        if graph[a][b] == INF:
            print("도달 불가", end=" ")
        else:
            print(graph[a][b], end=" ")
    print() #줄바꿈
