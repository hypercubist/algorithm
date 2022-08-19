import sys, heapq
input = sys.stdin.readline

INF = int(1e9)
n, e = map(int, input().split())
gh = [[] for _ in range(n+1)]

for i in range(e):
    a, b, c = map(int, input().split())
    gh[a].append((b, c))
    gh[b].append((a, c))

def dijkstra(start, target):
    distance = [INF] * (n+1)
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for i in gh[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    return distance[target]

v1, v2 = map(int, input().split())

#1 -> v1 -> v2 -> n
dist1 = dijkstra(1, v1) + dijkstra(v1, v2) + dijkstra(v2, n)
#1 -> v2 -> v1 -> n
dist2 = dijkstra(1, v2) + dijkstra(v2, v1) + dijkstra(v1, n)
total = 0
if dist1 < dist2:
    total = dist1
else:
    total = dist2

if total >= INF:
    print(-1)
else:
    print(total)