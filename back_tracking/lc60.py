# Permutation Sequence
import math


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        result = []
        nums = [x for x in range(1, n+1)]
        k -= 1

        while n > 0:
            n -= 1
            q, r = divmod(k, math.factorial(n))
            result.append(nums[q])
            nums.pop(q)
            k = r

        return "".join(map(str, result))
