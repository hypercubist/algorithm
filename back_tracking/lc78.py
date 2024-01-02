# Subsets

class Solution:
    def subsets(self, nums):

        def bt(st, sub):
            result.append(sub[:])

            for i in range(st, len(nums)):
                sub.append(nums[i])
                bt(i+1, sub)
                sub.pop()

        result = []
        bt(0, [])
        return result