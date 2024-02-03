# 1514. Path with Maximum Probability

# 무향, 가중치 그래프
# 가중치는 양수, 다익스트라를 이용할 수 있을 것 같다
# 가중치를 더하지 않고 곱함, 연산만 바뀌었을 뿐 계속해서 양수이므로 비교하는데 무리없을 것

import heapq
class Solution:
    def maxProbability(self, n, edges, succProb, start_node, end_node):

        graph = [[] for _ in range(n)]
        probabilities = [0] * n # 확률그래프는 0으로 초기화, 도달할 수 없는 케이스는 0으로 남는다
        # 그래프 변환
        for i in range(len(edges)):
            a, b = edges[i]
            prob = succProb[i]
            # 무향 그래프 이므로 양쪽 방향으로 추가
            graph[a].append((b, prob))
            graph[b].append((a, prob))

        q = []
        # 시작 지점 확률은 1
        # 확률은 큰게 유리한 선택이므로 최대힙으로 사용
        heapq.heappush(q, (-1, start_node))
        probabilities[start_node] = 1
        while q:
            prob_, now = heapq.heappop(q)
            prob = -prob_ # 최대힙 변환 조정
            if probabilities[now] > prob:
                continue
            for v, p in graph[now]:
                next_prob = prob * p
                if next_prob > probabilities[v]:
                    probabilities[v] = next_prob
                    # 최대힙
                    heapq.heappush(q, (-next_prob, v))

        return probabilities[end_node]
