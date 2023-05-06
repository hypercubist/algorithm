import heapq as h
from collections import deque as d
import copy
n, m, v = map(int, input().split())

gh = [[] for _ in range(n+1)]
dfs_visit = [False] * (n+1)
bfs_visit = [False] * (n+1)

for i in range(m):
    a, b = map(int, input().split())
    gh[a].append(b)
    gh[b].append(a)


def dfs(vx, graph):
    dfs_visit[vx] = True
    print(vx, end=" ")
    heap = graph[vx]
    h.heapify(heap)
    while heap:
        node = h.heappop(heap)
        if not dfs_visit[node]:
            dfs(node, graph)


def bfs(vx, graph):
    q = d([])
    q.append(vx)
    while q:
        node = q.popleft()
        if not bfs_visit[node]:
            bfs_visit[node] = True
            print(node, end=" ")
            heap = graph[node]
            h.heapify(heap)
            while heap:
                item = h.heappop(heap)
                q.append(item)



dfs(v, copy.deepcopy(gh))
print()
bfs(v, copy.deepcopy(gh))