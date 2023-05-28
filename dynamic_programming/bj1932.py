n = int(input())

graph = []
for _ in range(n):
    arr = list(map(int, input().split()))
    graph.append(arr)

for i in range(1, n):
    arr = graph[i] #len=i+1
    for idx in range(i+1):
        if idx == 0:
            arr[idx] += graph[i-1][idx]
        elif idx == i:
            arr[idx] += graph[i-1][idx-1]
        else:
            arr[idx] += max(graph[i-1][idx-1], graph[i-1][idx])

print(max(graph[n-1]))