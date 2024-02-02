# Course Schedule
# 진입 차수를 제거하는 방법으로 위상정렬
# 모두 정렬된 경우 남은 진입 차수가 없어야 한다.
# 사이클이 발생하는 경우 진입 차수가 남게되므로 정렬할 수 없음을 알 수 있다

from collections import deque
class Solution:
    def canFinish(self, numCourses, prerequisites):
        n = numCourses
        indegrees = [0] * numCourses
        graph = [[] for _ in range(n)]
        for a, b in prerequisites:
            indegrees[a] += 1
            graph[b].append(a)

        q = deque([])
        for i in range(numCourses):
            if indegrees[i] == 0:
                q.append(i)

        while q:
            i = q.popleft()
            for v in graph[i]:
                indegrees[v] -= 1
                if indegrees[v] == 0:
                    q.append(v)

        for i in indegrees:
            if i != 0: # 남은 진입 차수가 있으면 사이클 발생
                return False

        return True