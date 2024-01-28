# 2022 KAKAO BLIND RECRUITMENT 양과 늑대

# dfs로 풀어야 할 것 같지만 백트래킹
# 중복되는 케이스가 생기므로 방문 기록
# 각각의 케이스를 어떻게 기록할 것인가 -> 방문처리는 binary data -> 10진수로 변경하여 hashmap에 저장
def solution(info, edges):
    visited = [0] * len(info)
    def bt(sheep, wolf, case):
        if sheep > wolf: # 탐색 종료 조건 확인
            complete_cases[case] = sheep # 현재 케이스에서 구할 수 있는 양의 수 기록
        else:
            return

        for p, c in edges:
            if visited[p] and not visited[c]: # 부모 노드는 방문했지만 자식 노드는 방문하지 않은 케이스를 찾는다.
                next_case = case + 2**c # 다음 케이스 생성, c인덱스가 True로 변경됨, 10진수로 변환해서 더함
                if next_case not in complete_cases: # 이미 확인한 케이스라면 pass
                    visited[c] = True # 방문 처리
                    if info[c] == 0: # 양, 늑대 카운트
                        bt(sheep+1, wolf, next_case)
                    else:
                        bt(sheep, wolf+1, next_case)
                    visited[c] = False # 방문 해제

    visited[0] = True # 0번 노드 방문
    decimal_case = 1 # 0번 노드 방문 케이스 생성 (i=0 True -> 2^0 = 1)
    complete_cases = {decimal_case: 1} # 구할 수 있는 양 1마리
    bt(1, 0, decimal_case)
    return max(complete_cases.values())
