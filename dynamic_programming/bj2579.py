n = int(input())
g = [0]

for _ in range(n):
    g.append(int(input()))

if n == 1:
    print(g[n])
else:
    dp = [0] * (n+1)
    dp[1] = g[1]
    dp[2] = g[1] + g[2]

    for i in range(3, n+1):
        dp[i] = max(dp[i-2], dp[i-3] + g[i-1]) + g[i]

    print(dp[n])
