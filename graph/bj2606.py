import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
gh = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    gh[a].append(b)
    gh[b].append(a)

v = [False] * (n+1)
count = 0
def dfs(s):
    global count
    v[s] = True
    count += 1
    for i in gh[s]:
        if not v[i]:
            dfs(i)

dfs(1)
print(count-1)
