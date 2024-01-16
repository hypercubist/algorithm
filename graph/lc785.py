# Is Graph Bipartite?

# Bipartite??
# 그래프의 노드를 집합 A, B로 나누었을 때 그래프의 모든 간선이 집합 A-B를 서로 연결하고 있어야 한다.
# 집합 내부의 노드는 서로 직접 연결되어 있지 않다.
# 간선을 따라 계속해서 다른 집합으로 이동하게 되는 것을 의미
# 다른 노드 V로 이동할 때 해당 노드가 집합 A에 속해야 한다면 집합 A내부의 어떤 노드와도 연결되어 있으면 안된다.
# 위 조건을 만족하면서 모든 간선을 사용한 경우 Bipartite하다고 할 수 있다.

class Solution:
    def isBipartite(graph):
        n = len(graph)
        edges = []
        set_a = set([])
        set_b = set([])

        # edge : x -> y
        for x in range(n):
            for y in graph[x]:

                if i in set_a:
                    if edge in set_a:
                        print(i, 1)
                        return False
                    set_b.add(edge)
                elif i in set_b:
                    if edge in set_b:
                        print(i, 2)
                        return False
                    set_a.add(edge)
                else:
                    if edge in set_a:
                        set_b.add(i)
                    elif edge in set_b:
                        set_a.add(i)


        return True









