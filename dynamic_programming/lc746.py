# 746. Min Cost Climbing Stairs

# 70번 문제와 유사하다. n번째 칸의 최소비용은 n-1번째와 n-2번째 칸의 최소비용으로 정해진다
# 점화식 f(n) = min(f(n-2), f(n-1))

class Solution:
    def minCostClimbingStairs(self, cost):
        n = len(cost)
        if n == 2:
            return min(cost)

        dp_table = [0] * n
        dp_table[0] = cost[0]
        dp_table[1] = cost[1]
        for i in range(2, n):
            dp_table[i] = min(dp_table[i-2], dp_table[i-1]) + cost[i]

        return min(dp_table[n-1], dp_table[n-2])


