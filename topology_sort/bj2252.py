from collections import deque
n, m = map(int, input().split())

indegree = [0] * (n+1)

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

q = deque()
for i in range(1, n+1):
    if indegree[i] == 0:
        q.append(i)

result = []
while q:
    item = q.popleft()
    result.append(item)
    for i in graph[item]:
        indegree[i] -= 1
        if indegree[i] == 0:
            q.append(i)

for x in result:
    print(x, end=' ')