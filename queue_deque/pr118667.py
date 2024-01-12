# 2022 KAKAO TECH INTERNSHIP 두 큐 합 같게 만들기

from collections import deque
def solution(queue1, queue2):
    answer = -2

    target, r = divmod(sum(queue1+queue2), 2)

    if r == 1: #합이 홀 수이면 동일하게 나눌 수 없다
        answer = -1

    que = deque([(i, num) for i, num in enumerate(queue1+queue2)])

    already_chk = []
    answers = []
    for _ in range(len(que)):
        if que[0][0] in already_chk:
            continue
        for i in range(len(que)-1): # 큐 전체를 다 더하면 의미없는 케이스 이므로 -1
            q_sum = 0
            for j in range(0, i+1):
                q_sum += que[j][1]
            if q_sum == target:
                if que[0][0] + que[i+1][0] >= len(queue1): # 더하기를 시작할 인덱스 2개
                    answers.append(que[0][0] + que[i+1][0] - len(queue1))
                else:
                    answers.append(que[0][0] + que[i+1][0] + len(queue1))
                already_chk.append(que[i+1][0])
            elif q_sum > target:
                break
        que.append(que.popleft())

    if len(answers) == 0:
        answer = -1
    else:
        answer = min(answers)

    return answer
# print(solution([3, 2, 7, 2], [4, 6, 5, 1]))
print(solution( [1, 2, 1, 2],[1, 10, 1, 2]))
# print(solution([1, 1], [1, 5]))








