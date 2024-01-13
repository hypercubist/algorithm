import sys

sys.setrecursionlimit(10**6)

n, k = map(int, input().split())
arr = list(map(int, input().split()))
count = 0
finish = False
tmp = [None] * len(arr)
def merge(array, p, q, r):
    global count, k, finish
    i = p
    j = q + 1
    t = 0

    while i <= q and j <= r:
        if array[i] <= array[j]:
            tmp[t] = array[i]
            i += 1
        else:
            tmp[t] = array[j]
            j += 1
        t += 1

    while i <= q:
        tmp[t] = array[i]
        t += 1
        i += 1
    while j <= r:
        tmp[t] = array[j]
        t += 1
        j += 1
    i = p
    t = 0
    while i <= r:
        count += 1
        if count == k:
            print(tmp[t])
            finish = True
        array[i] = tmp[t]
        i += 1
        t += 1


def merge_sort(array, p, r):
    if finish:
        return
    if p < r:
        q = (p + r) // 2
        merge_sort(array, p, q)
        merge_sort(array, q + 1, r)
        merge(array, p, q, r)


merge_sort(arr, 0, n-1)

if count < k:
    print(-1)