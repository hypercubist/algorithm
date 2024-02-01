# 디스크 컨트롤러

# 시간이 긴 작업은 다른 작업을 더 많이 지연시킨다
# 시간이 짧은 작업이 우선 순위를 가지도록 정렬
# 우선순위큐에 작업 시간을 기준으로 삽입해준다

import heapq
def solution(jobs):
    n = len(jobs)
    total_time = 0
    now = 0
    q = []
    heapq.heapify(jobs)
    heapq.heapify(q)
    while jobs:
        start_req_time, start_duration = heapq.heappop(jobs)
        if now < start_req_time:
            now = start_req_time

        now += start_duration
        total_time += start_duration

        while jobs:
            req_time, duration = heapq.heappop(jobs)
            if now > req_time:
                heapq.heappush(q, [duration, req_time])
            else:
                heapq.heappush(jobs, [req_time, duration])
                break

        while q:
            d, r = heapq.heappop(q)
            now += d
            total_time += (now - r)
            while jobs:
                req_time, duration = heapq.heappop(jobs)
                if now > req_time:
                    heapq.heappush(q, [duration, req_time])
                else:
                    heapq.heappush(jobs, [req_time, duration])
                    break

    answer = total_time // n

    return answer

print(solution([[0, 10], [4, 10], [5, 11], [15, 2]]))
