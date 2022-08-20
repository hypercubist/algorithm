import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
s = deque()
result = [0] * (n+1)
result[n] = -1
s.append(-1)
for i in range(1, n):
    if arr[n-i-1] < arr[n-i]:
        result[n-i] = arr[n-i]
    else:
        while True:
            num = s.pop()
            if num == -1:
                result[n-i] = num
                break
            if arr[n-i-1] < num:
                result[n-i] = num
                break
    s.append(result[n-i])

for i in range(1,n+1):
    print(result[i], end=' ')
