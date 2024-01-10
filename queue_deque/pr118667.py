# 2022 KAKAO TECH INTERNSHIP 두 큐 합 같게 만들기

from collections import deque
def solution(queue1, queue2):
    answer = -2

    q, r = divmod(sum(queue1) + sum(queue2), 2)
    if r == 1: # 두 큐의 합이 홀수인 경우 불가
        answer = -1

    que = deque([(i, num) for i, num in enumerate(queue1+queue2)])
    cases = []
    while True:







    return answer