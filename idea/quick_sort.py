# 퀵정렬의 평균 시간복잡도는 O(NlogN), 최악의 경우 O(N^2)

# 호어 분할 방식
def quick_sort(array, start, end):
    if start >= end:
        return
    pivot = start # 첫번째 원소를 피벗으로 지정
    left = start + 1 # 왼쪽은 두번째 원소 (피벗 다음)
    right = end # 오른쪽은 마지막 원소
    while left <= right:
        while left <= end and array[left] <= array[pivot]: # 왼쪽에서 오른쪽으로 진행하며 피벗보다 큰 데이터를 찾는다.
            left += 1
        while right > start and array[right] >= array[pivot]: # 오른쪽에서 왼쪽으로 진행하며 피벗보다 작은 데이터를 찾는다.
            rihgt -= 1
        # 피벗을 기준으로 데이터를 찾은 후에 서로 엇갈렸는지 판단하여 분기한다.
        if left > right: # 엇갈렸다면 작은 데이터와 피벗을 교체한 후 해당 사이클 교체를 마무리한다.
            array[right], array[pivot] = array[pivot], array[right]
        else: # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체하고 계속해서 교체를 진행한다.
            array[left], array[right] = array[right], array[left]