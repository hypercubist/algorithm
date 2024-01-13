# n개의 숫자는 카운팅하고 m개의 숫자는 배열에 담아서 카운터에서 조회하는 방법으로
from collections import Counter

n = int(input())
n_list = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))

n_cnt = Counter(n_list)

for i in m_list:
    print(n_cnt[i], end=" ")
