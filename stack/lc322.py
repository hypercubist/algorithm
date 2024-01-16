# Coin Change

#
class Solution:
    def coinChange(self, coins, amount):
        coins.sort(reversed = True)

        total = 0

        for i in range(len(coins)):
            coin = coins[i]
            q, r = divmod(amount, coin)
            total += q
            if r == 0:
                break
            elif r in coins:
                total += 1
                break
            else:
                amount = r


