# 2022 KAKAO BLIND RECRUITMENT 신고 결과 받기

# 신고한 사람을 set에 담아 관리

from collections import defaultdict
def solution(id_list, report, k):
    n = len(id_list) # 사람 수
    answer = [0] * n # 정답 리스트, 메일 받을 횟수 0으로 초기화
    
    id_dict = {} # id별로 인덱스를 담을 dict
    for i in range(n):
        id_dict[id_list[i]] = i

    # 각각의 사람을 (신고한 사람들)을 담을 set default dict
    # 신고한 사람들을 set에 담으므로 중복 신고는 제거됨
    # 신고한 사람, 신고당한 사람 모두 인덱스로 담을 것
    dd = defaultdict(set)
    
    for r in report:
        sniper, target = r.split(' ')
        dd[id_dict[target]].add(id_dict[sniper]) # 신고한 사람, 신고당한 사람 모두 인덱스로 담음

    for target, snipers in dd.items():
        if len(snipers) >= k: # target을 신고한 sniper가 k명 이상인 경우
            for sniper in snipers: # 각 sniper에게 메일 발송
                answer[sniper] += 1 # 메일 발송 횟수 누적

    return answer
