# 다익스트라로 풀어야 할 것 같지만 벨만포드 공부한 김에 해봄

import sys
input = sys.stdin.readline

INF = 1e9

n = int(input())
m = int(input())
graph = []
for _ in range(m):
    a, b, c = map(int, input().split())
    graph.append((a, b, c))
s, e = map(int, input().split())

def bf(gh, s, e):
    dist = [INF] * (n+1)
    dist[s] = 0
    changed = True
    while changed:
        changed = False
        for bus in gh:
            a = bus[0]
            b = bus[1]
            cost = bus[2]
            if dist[b] > dist[a] + cost:
                dist[b] = dist[a] + cost
                changed = True
    return dist[e]

print(bf(graph, s, e))
