import sys
input = sys.stdin.readline


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


t = int(input())
for _ in range(t):

    n, m = map(int, input().split())
    p= [0] * (n+1)
    # e = [[] for _ in range(n+1)]
    for i in range(n+1):
        p[i] = i
    count = 0
    for _ in range(m):
        a, b = map(int, input().split())
        if find(a) != find(b):
            union(a, b)
            count += 1
    print(count)