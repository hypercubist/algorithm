#선택정렬은 시간복잡도 O(N^2)으로 다른 알고리즘에 비해 비효율적이다
#다만, 특정한 리스트에서 가장 작은 데이터를 찾는 일이 잦으므로 소스코드 형태에 익숙해질 필요가 있다.

def selection_sort(array):
    for i in range(len(array)):
        min_idx = i #정렬되지 않은 원소 중 가장 앞 쪽 원소를 최소값으로 잡고
        for j in range(i+1, len(array)): #배열 내 최소값의 인덱스를 찾는 과정
            if array[min_idx] > array[j]:
                min_idx = j
        array[i], array[min_idx] = array[min_idx], array[i] #찾고나서 정렬되  않은 원소 중 가장 앞 쪽 원소와 swap
    return arrayz