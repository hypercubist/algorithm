import sys

input = sys.stdin.readline

arr = []
k = int(input())
for _ in range(k):
    x = int(input())
    if x == 0:
        arr.pop()
    else:
        arr.append(x)

print(sum(arr))