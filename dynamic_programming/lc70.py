# 70. Climbing Stairs

# 점화식 f(n) = f(n-1) + f(n-2)

# top down
class Solution:
    def climbStairs(self, n):
        if n == 1:
            return 1
        if n == 2:
            return 2
        dp_table = [0] * (n + 1)
        dp_table[1] = 1
        dp_table[2] = 2

        def dp(x):
            if dp_table[x] != 0:
                return dp_table[x]
            else:
                dp_table[x] = dp(x-1) + dp(x-2)
                return dp_table[x]

        return dp(n)


# bottom up
class Solution:
    def climbStairs(self, n):
        if n == 1:
            return 1
        if n == 2:
            return 2
        dp_table = [0] * (n + 1)
        dp_table[1] = 1
        dp_table[2] = 2

        for i in range(3, n + 1):
            dp_table[i] = dp_table[i-2] + dp_table[i-1]

        return dp_table[n]


