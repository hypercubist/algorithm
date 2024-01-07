# 2019 KAKAO BLIND RECRUITMENT 후보키

# 후보키 : 튜플을 구분할 수 있는 유일하면서 최소인 속성의 집합
# 속성(col) > 인덱스로 지정
# 유일성 > 속성을 지정한 후 튜플을 탐색해서 중복이 있는지 확인
# 튜플을 문자열로 붙인 다음 set에 넣어서 원래 갯수보다 적어지면 중복이 있는 것임
# 완전탐색으로 조회해도 시간초과되지 않는다

# 최소성을 만족해야 하므로 속성(컬럼)을 1개만 선택한 것부터 조합(속성들의 조합)을 만들어 속성을 늘려가며 확인한다.
# 이미 유일성을 만족한 속성이 있는 경우 해당 속성을 포함한 다른 조합의 경우 pass한다.

def solution(relation):
    n = len(relation)
    m = len(relation[0])
    candids = [] # 후보키 집합

    #속성을 target_cnt개 조합하여 리턴
    def get_combis(start, target_cnt, cnt, result, now):
        # 속성을 target_cnt개 고를 때까지 조합한다.
        if cnt == target_cnt:
            result.append(now[:])
            return
        for col in range(start, m):
            now.append(col)
            get_combis(col+1, target_cnt, cnt+1, result, now)
            now.pop()


    def is_unique(relation, cols): # attrs > 속성 인덱스가 나열된 배열
        binding_strs = ["" for _ in range(n)]
        for attr in cols:
            col = [item[attr] for item in relation]
            binding_strs = [a+"|"+b for a, b in zip(binding_strs, col)]
        if len(set(binding_strs)) < n:
            return False
        else:
            return True

    # 속성 갯수를 늘려가면서 확인
    for i in range(1, n+1):
        combis = [] # 속성을 i개 선택한 조합
        get_combis(0, i, 0, combis, [])

        for cols in combis:
            is_min = True
            for candid in candids:
                # 이미 추가된 후보키들이 부분집합인 경우 최소성을 만족하지 않으므로 유일성을 확인할 필요없다.
                if set(candid).issubset(set(cols)):
                    is_min = False
                    break

            if not is_min:
                continue

            # 유일성
            if is_unique(relation, cols):
                candids.append(cols)
    return len(candids)





print(solution([["100", "ryan", "music", "2"], ["200", "apeach", "math", "2"], ["300", "tube", "computer", "3"], ["400", "con", "computer", "4"], ["500", "muzi", "music", "3"], ["600", "apeach", "music", "2"]]))