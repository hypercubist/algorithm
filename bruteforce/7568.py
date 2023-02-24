# 모두 비교해야하나?...

n = int(input())
arr = []
rank = [0] * n
for _ in range(n):
    x, y = map(int, input().split())
    arr.append((x, y))

for i in range(len(arr)):
    count = 0
    for x in arr:
        if arr[i][0] < x[0] and arr[i][1] < x[1]:
            count += 1
    rank[i] = count + 1

for i in rank:
    print(i, end=" ")



