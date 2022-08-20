import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

def find(x):
    if p[x] != x:
        p[x] = find(p[x])
    return p[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        p[b] = a
    else:
        p[a] = b

n, m = map(int, input().split())
p = [0] * (n+1)
for i in range(n+1):
    p[i] = i

for i in range(m):
    exp, a, b = map(int, input().split())
    if exp == 0:
        if find(a) != find(b):
            union(a, b)
    else:
        if find(a) == find(b):
            print('YES')
        else:
            print('NO')