# 힙 라이브러리를 사용해서 구현
# 파이썬 힙은 루트노드가 가장 작은 최소힙이다.
# 배열을 힙에 넣었다 빼주면 NlogN 시간에 오름차순으로 정렬된다.
import heapq

def heap_sort(array):
    arr = array.copy()
    heapq.heapify(arr)  # 힙 구성
    return [heapq.heappop(arr) for _ in range(len(arr))]
