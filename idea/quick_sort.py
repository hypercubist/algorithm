# 퀵정렬의 평균 시간복잡도는 O(NlogN), 최악의 경우 O(N^2)

# 호어 분할 방식
def quick_sort(array, start, end):
    if start >= end:
        return
    pivot = start # 첫번째 원소를 피벗으로 지정
    left = start + 1 # 왼쪽은 두번째 원소 (피벗 다음)
    right = end # 오른쪽은 마지막 원소
    while left <= right: # 왼쪽과 오른쪽이 같을 때는 피벗을 포함하여 정렬할 데이터가 2개 밖에 없을 때이다. 이 때도 정렬은 필요하다.
        while left <= end and array[left] <= array[pivot]: # 왼쪽에서 오른쪽으로 진행하며 피벗보다 큰 데이터를 찾는다.
            left += 1
        while right > start and array[right] >= array[pivot]: # 오른쪽에서 왼쪽으로 진행하며 피벗보다 작은 데이터를 찾는다.
            right -= 1
        # 피벗을 기준으로 데이터를 찾은 후에 서로 엇갈렸는지 판단하여 분기한다.
        if left > right: # 엇갈렸다면 작은 데이터와 피벗을 교체한 후 해당 사이클 교체를 마무리한다.
            array[right], array[pivot] = array[pivot], array[right]
        else: # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체하고 계속해서 교체를 진행한다.
            array[left], array[right] = array[right], array[left]

            
# 파이썬을 활용한 퀵 정렬 소스코드
def quick_sort2(array):
    #리스트에 원소가 하나일 경우 정렬할 필요없음
    if len(array) <= 1:
        return array

    pivot = array[0] #피벗 설정
    tail = array[1:] #피벗을 제외한 리스트

    left = [x for x in tail if x <= pivot]
    right = [x for x in tail if x > pivot]
    #분할하여 각각 정렬한 후 합쳐서 리턴
    return quick_sort2(left) + [pivot] + quick_sort2(right)

