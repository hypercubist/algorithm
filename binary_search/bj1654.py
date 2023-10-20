# 파라메트릭 서치

k, n = map(int, input().split())

lan_cables = []
for _ in range(k):
    lan_cables.append(int(input()))

# 자를 수 있는 사이즈 중 가장 큰 값을 찾기
# result값의 번위 0 < result < max(lan_cables)

def counting(arr, leng):
    count = 0
    for x in arr:
        count += x // leng
    return count

def bin(arr, t, s, e):
    result = 0
    while s <= e:
        mid = (s + e) // 2
        if counting(arr, mid) >= n:
            result = mid
            s = mid + 1
        else:
            e = mid - 1
    return result


answer = bin(lan_cables, n, 1, max(lan_cables))
print(answer)
