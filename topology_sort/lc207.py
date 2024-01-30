# Course Schedule

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
            if i != 0:
                return False

        return True