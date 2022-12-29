#이진검색은 먼저 데이터가 정렬이 되어야 한다.
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