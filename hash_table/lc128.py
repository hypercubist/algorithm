# 128. Longest Consecutive Sequence

# 해시맵으로 시간줄이기
class Solution:
    def longestConsecutive(self, nums):
        max_count = 0

        nums_hash_set = {}
        for num in nums:
            nums_hash_set[num] = True

        for num in nums:
            if num - 1 not in nums_hash_set:
                count = 1
                next = num + 1
                while next in nums_hash_set:
                    count += 1
                    next += 1
                max_count = max(max_count, count)

        return max_count
