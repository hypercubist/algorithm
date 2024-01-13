# 조합?

from itertools import combinations

n, target = map(int, input().split())
cards = map(int, input().split())

winner = 0
gap = 1e9
for c in combinations(cards, 3):
    card_sum = sum(c)
    gap_temp = target-card_sum
    if 0 <= gap_temp <= gap:
        winner = card_sum
        gap = target-card_sum
        if gap_temp == 0:
            break

print(winner)


