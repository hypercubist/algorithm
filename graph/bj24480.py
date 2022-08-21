import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

n, m, r = map(int, input().split())
visited = [0] * (n + 1)
gh = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    gh[a].append(b)
    gh[b].append(a)

count = 0
def dfs(start, visited):
    global count
    count += 1
    visited[start] = count
    gh[start].sort(reverse=True)
    for i in gh[start]:
        if visited[i] == 0:
            dfs(i, visited)

dfs(r, visited)

for i in range(1, n+1):
    print(visited[i])