# combination
# 조합은 이전에 선택한 것을 배제해야하므로 먼저 선택한 수 보다 큰 수부터 순회하도록 하는 것이 포인트
# 정렬되어 있으므로 가능
def combine(self, n, k):

    result = []
    bucket = []
    def bt(select):
        if len(bucket) == k:
            result.append(bucket[:])
            return
        for i in range(select+1, n+1): #범위를 먼저 선택한 수 보다 큰 수부터 순회
            bucket.append(i)
            bt(i)
            bucket.pop()

    bt(0)
    return result