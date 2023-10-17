# 파라메트릭 서치 문제
# 단정 문제로 변경하기
import sys

input = sys.stdin.readline
n, c = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))
arr.sort()
full_range = arr[-1] - arr[0]
max_result = full_range // (c - 1)

def bin_search(array, t, s, e):
    result = -1
    while s <= e:
        mid = (s + e) // 2
        possible = positioning(array, mid, t)

        if possible: #여유있다. 간격 늘리자. 이건 답이 될 수 있는 케이스이므로 기록한다.
            result = mid
            s = mid + 1
        else:
            e = mid - 1
    return result


def positioning(array, interval, target):
    count = 1
    left = 0
    right = 1
    while right < n:
        if array[right] >= array[left] + interval:
            count += 1
            left = right
        right += 1

    return count >= target


print(bin_search(arr, c, 1, max_result))