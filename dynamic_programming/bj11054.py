n = int(input())
arr = list(map(int, input().split()))

dp_n = [1] * n
dp_r = [1] * n

for i in range(1, n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp_n[i] = max(dp_n[i], dp_n[j]+1)

arr.reverse()
for i in range(1, n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp_r[i] = max(dp_r[i], dp_r[j]+1)

dp_r.reverse()
dp_result = [dp_n[x] + dp_r[x] for x in range(n)]

print(max(dp_result) - 1)