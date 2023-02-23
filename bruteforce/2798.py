# 조합?

from itertools import combinations

n, target = map(int, input().split())
cards = map(int, input().split())

winner = 0
gap = target
for c in combinations(cards, 3):
    card_sum = sum(c)
    gap_temp = card_sum-target
    if 0 <= gap_temp <= gap:
        winner = card_sum
        gap = card_sum-target
        if gap_temp == 0:
            break

print(winner)


