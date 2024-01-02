# binary search
class Solution:
    def search(self, nums, target):
        def bs(arr, s, e, t):
            if s > e:
                return -1
            mid = (s + e) // 2
            if arr[mid] == t:
                return mid
            elif arr[mid] > t:
                return bs(arr, s, mid - 1, t)
            else:
                return bs(arr, mid + 1, e, t)

        return bs(nums, 0, len(nums)-1, target)