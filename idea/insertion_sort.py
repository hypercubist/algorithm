# 시간복잡도 O(N^2)
# 이미 정렬이 되어있을 수록 빠르다. 최선의 경우 O(N)
# 확인 중인 인덱스 왼쪽의 원소들은 모두 오름차순 정렬되어 있다(오름차순 기준)

def insertion_sort(array):
    for i in range(1, len(array)):
        for j in range(i, 0, -1): # i to 1, 확인 중인 원소를 왼쪽의 정렬된 원소들과 비교
            if array[j] < array[j-1]: # 왼쪽이 더 크면 바꾸고
                array[j], array[j-1] = array[j-1], array[j],
            else: # 왼쪽이 작은 경우에는 멈추면 된다. (이미 정렬되어 있음)
                break
    return array