#모든 데이터가 정수 형태일 때만 사용 가능, 일반적으로 가장 작은 데이터와 가장 큰 데이터의 차이가 1,000,000을 넘지 않을 때 효과적
#데이터의 개수가 N, 데이터 중 최댓값이 K일 때, 최악의 경우에도 O(N+K)를 보장
#데이터의 크기가 한정되어 있고, 데이터의 크기에 중복이 많을수록 유리

def count_sort(array):
    #각 데이터를 카운트할 리스트 초기화(모든 데이터를 포함할 수 있는 범위)
    count = [0] * (max(array) + 1)

    for i in range(len(array)):
        count[array[i]] += 1

    result = []
    for i in range(len(count)): #카운트된 정보 확인
        for j in range(count[i]): #카운트 횟수만큼 붙이기
            result.append(i)

    return result