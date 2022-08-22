import sys
sys.stdin.readline
sys.setrecursionlimit(10**6)
v = int(input())

gh = [[] for _ in range(v+1)]



for i in range(1, v+1):
    arr = list(map(int, input().split()))[1:]
    idx = 0
    while arr[idx] != -1:
        gh[i].append((arr[idx], arr[idx+1]))
        idx += 2
print(gh)
visited = [False] * (v+1)
max_d = 0
max_i = 0
def dfs(start, distance):
    global max_d, max_i
    if max_d < distance:
        max_d = distance
        max_i = start
    visited[start] = True
    for i in gh[start]:
        next, dist = i
        if not visited[next]:
            dfs(next, distance + dist)
dfs(1, 0)
visited = [False] * (v+1)
dfs(max_i, 0)

print(max_d)
