# 리스트를 반복해서 분할하여 새로운 리스트를 만들고 각각 비교하여 병합하면서 정렬된 리스트 만든다.
# 공간을 많이 차지한다.
# 메모리에 한 번에 들어가지 않는 대용량의 데이터도 분할하여 정렬 가능
# 다중 코어를 활용하여 병렬처리가 가능하다

def merge_sort(array):
    if len(array) <= 1:
        return array  # 배열의 원소가 1개이면 정렬할 필요가 없다.

    mid = len(array) // 2

    # 분할
    left = merge_sort(array[:mid])  # 재귀적으로 정렬
    right = merge_sort(array[mid:])  # 재귀적으로 정렬

    # 병합
    return merge(left, right)


def merge(left, right):
    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):  # 왼쪽 또는 오른쪽 배열의 원소를 모두 소진할 때까지
        if left[i] <= right[j]:  # 양쪽 배열의 첫번째 원소 중 더 작은 것 = 양쪽 배열의 모든 원소 중 가장 작은 원소 (각 배열은 이미 오름차순 정렬돼있으므로)
            result.append(left[i])
            i += 1  # 다음 인덱스
        else:
            result.append(right[j])
            j += 1

    if i < len(left):  # 왼쪽 배열에 원소가 남아있으면 (오른쪽은 모두 소진함)
        result.extend(left[i:])  # 남은 원소들은 result에 담겨있는 원소보다 크고 오름차순 정렬돼있다. 그냥 이어 붙이면 완성
    if j < len(right):
        result.extend(right[j:])

    return result
