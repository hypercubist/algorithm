import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
n = int(input())
graph = [[] for _ in range(n+1)]
visited = [False] *(n+1)
parent = [0] * (n+1)
for i in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(x):
    visited[x] = True
    for i in graph[x]:
        if not visited[i]:
            parent[i] = x
            dfs(i)

dfs(1)
for i in range(2, n+1):
    print(parent[i])