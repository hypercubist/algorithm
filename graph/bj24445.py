import sys
from collections import deque

def bfs(g, s, v, c):
    v[s] = c
    q = deque([s])
    while q:
        now = q.popleft()
        for i in sorted(g[now],reverse=True):
            if v[i] == 0:
                c += 1
                v[i] = c
                q.append(i)

input = sys.stdin.readline

n, m, r = map(int, input().split())
gh = [[] for _ in range(n+1)]
visited = [0] * (n+1)
for _ in range(m):
    a, b = map(int, input().split())
    gh[a].append(b)
    gh[b].append(a)

bfs(gh, r, visited, 1)

for i in range(1, n+1):
    print(visited[i])