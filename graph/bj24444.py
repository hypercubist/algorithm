from collections import deque

def bfs(s, graph, visited):
    count = 1
    q = deque()
    visited[s] = count
    q.append(s)
    while q:
        v = q.popleft()
        for i in sorted(graph[v]):
            if visited[i] == 0:
                count += 1
                visited[i] = count
                q.append(i)

n, m, r = map(int, input().split())
visited = [0] * (n+1)
gh = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    gh[a].append(b)
    gh[b].append(a)

bfs(r, gh, visited)
for i in range(1, n+1):
    print(visited[i])

