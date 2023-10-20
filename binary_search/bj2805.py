# 파라메트릭 서치

n, m = map(int, input().split())
namus = list(map(int, input().split()))


# H가 가능한 범위 0 <= H <= max(namus)

def cutting(arr, height):
    total = 0
    for x in arr:
        namu_tomak = x - height
        if namu_tomak > 0:
            total += namu_tomak
    return total

def bin(arr, t, s, e):
    result = 0
    while s <= e:
        mid = (s + e) // 2
        if cutting(arr, mid) >= t:
            result = mid
            s = mid + 1
        else:
            e = mid - 1
    return result

print(bin(namus, m, 0, max(namus)))