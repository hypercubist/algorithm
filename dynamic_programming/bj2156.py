import sys
input = sys.stdin.readline
n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))

dp = [0] * n
for i in range(n):
    if i == 0:
        dp[i] = arr[i]
    elif i == 1:
        dp[i] = arr[i-1] + arr[i]
    elif i == 2:
        dp[i] = max(arr[i-2]+arr[i-1], arr[i-1]+arr[i], arr[i]+arr[i-2])
    else:
        dp[i] = max(dp[i-2]+arr[i], dp[i-3]+arr[i-1]+arr[i], dp[i-1])

print(dp[n-1])