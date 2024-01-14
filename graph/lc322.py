# Coin Change

# 동전 간의 관계가 배수가 아니면 그리디는 불가
# 매 번 동전을 선택할 때를 분기해서 완전탐색
# 최소 갯수를 선택해야하므로 dfs보다 bfs가 유리하다

from collections import deque
class Solution:
    def coinChange(self, coins, amount):

        q = deque([(amount, 0)])
        visited = set() # 완전탐색하다보면 이미 계산한 케이스를 다시 반복할 수 있다. 잔돈이 이미 확인했었던 금액이면 pass하기 위한 set
        while q:
            change, count = q.popleft()
            if change == 0:
                return count # bfs로 확인하므로 잔액이 0원 확인되는 즉시 최소 카운트임을 알 수 있다.
            for coin in coins:
                next = change - coin
                if next not in visited and next >= 0: # 잔돈을 남길 수 있는 조건을 먼저 확인하고 다음 단계를 설정하고 큐에 넣어준다.
                    q.append((next, count + 1))
                    visited.add(next)

        return -1
