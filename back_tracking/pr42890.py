# 2019 KAKAO BLIND RECRUITMENT 후보키

# 후보키 : 튜플을 구분할 수 있는 유일하면서 최소인 속성의 집합
# 속성(col) > 인덱스로 지정
# 유일성 > 속성을 지정한 후 튜플을 탐색해서 중복이 있는지 확인
# 최소성 > 속성을 한 개부터 지정해서 유일성을 확인 > 유일성이 확인된 순간 최소성 만족 > 해당 속성 집합에 속성을 더 추가할 필요가 없다.
# 최소성을 만족하지 않는 경우 속성을 추가해서 확인

# 튜플을 문자열로 붙인 다음 set에 넣어서 원래 갯수보다 적어지면 중복이 있는 것임
def solution(relation):
    n = len(relation)
    m = len(relation[0])
    selected = [] # 선택된 속성들
    result = [] # 후보키 집합
    # 속성이 주어지면 유일성을 확인한다.
    def is_unique(attrs): # attrs > 속성 인덱스가 나열된 배열
        binding_strs = ["" for _ in range(n)]
        for attr in attrs:
            col = [item[attr] for item in relation]
            binding_strs = [a+"|"+b for a, b in zip(binding_strs, col)]
        if len(set(binding_strs)) < n:
            return False
        else:
            return True

    def bt(start_idx):
        for j in range(start_idx, m):
            # j > 속성 선택
            if [j] not in result:
                selected.append(j)
                if is_unique(selected):
                    result.append(selected[:])
                else:
                    # 백트래킹: 추가 속성 선택
                    bt(j+1)
                selected.pop()
    
    for i in range(m): # 단일 속성 후보키 먼저 등록
        if is_unique([i]):
            result.append([i])

    bt(0)
    return len(result)

test = [["100", "ryan", "music", "2"], ["200", "apeach", "math", "2"], ["300", "tube", "computer", "3"], ["400", "con", "computer", "4"], ["500", "muzi", "music", "3"], ["600", "apeach", "music", "2"]]

print(solution(test))