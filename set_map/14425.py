# m개의 문자열은 중복이 있을 수 있으므로 카운터로 반복 횟 수를 줄여주면 될 것 같다.
from collections import Counter

n, m = map(int, input().split())
s1 = []
s2 = []
for _ in range(n):
    s1.append(input())

for _ in range(m):
    s2.append(input())
ct1 = Counter(s1)
ct2 = Counter(s2)
ct_result = ct2 - ct1 #차집합

sum = 0
for k, v in ct_result.items():
    sum += v

print(m-sum)




