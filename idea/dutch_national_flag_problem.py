# 섞여있는 세 가지 원소를 정렬하는 문제
# 시간복잡도 O(N)으로 해결이 가능하다.

# 배열 안의 원소는 0, 1, 2 셋 중 하나
arr = [1, 2, 0, 0, 1, 1, 0, 2, 0, 2, 1, 0]
def dutch(array):
    # 3pointers
    left = 0
    mid = 0
    right = len(array) - 1

    while mid <= right:
        if array[mid] == 0:
            array[left], array[mid] = array[mid], array[left]
            left += 1
            mid += 1
        elif array[mid] == 1:
            mid += 1
        else:
            array[mid], array[right] = array[right], array[mid]
            right -= 1

dutch(arr)
print(arr)