# 음.. 딱 봐도 교집합인데
import sys
from collections import Counter
input = sys.stdin.readline
n, m = map(int, input().split())

nlist = []
mlist = []
for _ in range(n):
    nlist.append(input().strip())
for _ in range(m):
    mlist.append(input().strip())

ncnt = Counter(nlist)
mcnt = Counter(mlist)
cross_cnt = ncnt & mcnt
print(len(cross_cnt))
for i in sorted(cross_cnt):
    print(i)
