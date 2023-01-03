#이진탐색은 먼저 데이터가 정렬이 되어야 한다.

# 반복문으로 구현
def binary_search(array, value):
    left = 0
    right = len(array) - 1
    while left <= right:
        mid = (left + right) // 2 #중앙값
        if array[mid] == value: #찾으면 인덱스 리턴
            return mid
        elif array[mid] < value:
            left = mid + 1
        else:
            right = mid - 1
    return -1 #못찾은 경우

# 재귀함수로 구현, left ~ right 파라미터로 검색 구간을 설정할 수 있음
def binary_search2(array, value, left, right):
    if left > right:
        return -1
    mid = (left + right) // 2
    if array[mid] == value:
        return mid
    elif array[mid] < value:
        return binary_search2(array, value, mid+1, right)
    else:
        return binary_search2(array, value, left, mid-1)