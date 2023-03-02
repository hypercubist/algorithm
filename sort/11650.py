import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    x, y = map(int, input().split())
    arr.append((x, y))

for item in sorted(arr):
    print(item[0], end=" ")
    print(item[1])