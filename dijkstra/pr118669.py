# 2022 KAKAO TECH INTERNSHIP 등산코스 정하기

# 휴식없이 이동해야하는 시간 중 가장 긴 시간이 intensity가 되므로 한 번 긴 구간을 지나치면 더 짧은 구간을 지나도 무의미하다
# 그러므로 출입구 -> 봉우리 이동 중 지나친 경로를 최선으로 선택하고 그대로 돌아오는 방법이 최선이다.
# 그러므로 출입구 -> 봉우리로 올라가는 케이스만 생각하면 된다.
# 각 출입구에서 각 봉우리로 올라가는 길 중 intensity가 가장 작은 길을 찾으면 완료

# 다익스트라로 각 노드에서 최선을 기록하면서 봉우리까지 도달
# 출입구 별로 케이스, 케이스 외의 출입구가 포함된 엣지는 제외한다.
# 봉우리에 도달하면 정지
# 케이스별로 intensity 구한 후 가장 작은 값 확인

import heapq
def solution(n, paths, gates, summits):
    graph = [[] for _ in range(n+1)]
    gates_set = set(gates)  # 진행 중 노드가 출입구 또는 봉우리 인지 수시로 확인해야 하므로 set
    summits_set = set(summits)  # 진행 중 노드가 봉우리인지 수시로 확인해야 하므로 set
    intensity_q = [(1e9, -1)] # intensity 최소값들을 담을 힙큐, 최상단 노드와 비교를 위해 INF값 세팅

    for i, j, w in paths:   # 그래프 변환
        graph[i].append((j, w))
        graph[j].append((i, w))

    for gate in gates:  # 각 출입구 별 케이스
        intensity = [1e9] * (n+1)   # intensity 배열 초기화
        q = []
        intensity[gate] = 0 # gate가 start node
        heapq.heappush(q, (0, gate))

        while q:
            now_ints, now = heapq.heappop(q)
            if intensity[now] < now_ints:
                continue
            for v, ints in graph[now]:
                if v not in gates_set: # 출입구의 경우 진행하지 않는다
                    next_ints = max(ints, now_ints)
                    if next_ints < intensity[v]:
                        intensity[v] = next_ints
                        if v not in summits_set:    # 봉우리에서 정지, 다음 노드가 봉우리가 아닌 경우에만 힙큐에 추가
                            heapq.heappush(q, (next_ints, v))

        for summit in summits: # 봉우리 인덱스만 확인해서 힙큐에 저장
            if intensity[summit] <= intensity_q[0][0]: # 최상단 노드와 비교해서 삽입
                heapq.heappush(intensity_q, (intensity[summit], summit))

    result_intensity, result_summit = heapq.heappop(intensity_q)
    return [result_summit, result_intensity]

print(solution(6, [[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]], [1, 3], [5]))