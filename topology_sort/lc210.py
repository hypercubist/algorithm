# 210. Course Schedule II
# 위상정렬
# 정렬된 순서를 반환
# 순서는 결국 큐에서 나온 순서이므로 큐에서 나올 때 순서 기록

import heapq
class Solution:
    def findOrder(self, numCourses, prerequisites):
        # 그래프 생성
        graph = [[] for _ in range(numCourses)]

        # 진입차수 초기화 및 그래프 변환
        idgs = [0] * numCourses
        for a, b in prerequisites:
            idgs[a] += 1
            graph[b].append(a)

        # 큐 생성, 시작 노드 삽입(진입차수=0)
        q = []
        for i in range(numCourses):
            if idgs[i] == 0:
                heapq.heappush(q, i)

        # 순서 저장할 배열
        order = []
        while q:
            i = heapq.heappop(q)
            order.append(i)
            for v in graph[i]:
                idgs[v] -= 1
                if idgs[v] == 0:
                    heapq.heappush(q, v)

        # 모든 노드가 정렬된 경우
        if len(order) == numCourses:
            return order
        else:
            return []




