# 743. Network Delay Time

# k -> n 최단거리 구해라
# 방향그래프, 가중치 있음, 가중치 양수 -> 다익스트라

import heapq
class Solution:
    def networkDelayTime(self, times, n, k):
        # 최단거리 테이블
        distance = [1e9] * (n+1)

        graph = [[] for _ in range(n+1)]
        for item in times:
            u, v, w = item
            graph[u].append((v, w))

        q = []
        heapq.heappush(q, (0, k))
        distance[0] = 0
        distance[k] = 0
        while q:
            dist, now = heapq.heappop(q)
            if distance[now] < dist:
                continue
            for v, c in graph[now]:
                next_dist = dist + c
                if next_dist < distance[v]:
                    distance[v] = next_dist
                    heapq.heappush(q, (next_dist, v))

        min_time = max(distance)
        if min_time == 1e9:
            return -1
        return min_time