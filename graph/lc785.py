# Is Graph Bipartite?

# 이분 그래프??
# 같은 집합 내 연결된 노드가 없어야한다
# 간선을 따라 이동할 때 마다 집합이 달라져야 한다. (계속해서 다른 집합으로 이동)

# dfs, bfs ? 모든 노드를 이어 방문하면서 집합을 선정하고 예상했던 집합이 아닌 케이스를 찾는다.

from collections import deque
class Solution:
    def isBipartite(self, graph):

        set_list = [-1 for _ in range(len(graph))] # -1(미확인), 0(setA), 1(setB)

        for i, s in enumerate(set_list):
            # 이렇게 모든 노드에 대해서 출발을 설정하면 이어지지 않은 다른 노드들도 확인할 수 있다.(완전탐색에서 확인하지 못한 노드들)
            if s == -1:
                q = deque([i])
                set_list[i] = 0 #set 0으로 정하기
                while q:
                    x = q.popleft() # x -> y
                    for y in graph[x]:
                        if set_list[y] == -1: # 아직 다음 노드의 집합이 결정되지 않았으면
                            set_list[y] = set_list[x] ^ 1 # 출발 노드와 다른 집합에 넣음
                            q.append(y)
                        elif set_list[x] == set_list[y]:
                            return False

        return True

