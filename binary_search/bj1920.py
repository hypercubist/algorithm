from bisect import bisect_left, bisect_right
n = int(input())
arr = list(map(int, input().split()))
arr.sort()
m = int(input())
arr2 = list(map(int, input().split()))

for i in range(m):
    left = bisect_left(arr, arr2[i])

    if left < n and arr[left] == arr2[i]:
        print(1)
    else:
        print(0)