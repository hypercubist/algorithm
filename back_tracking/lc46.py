#permutations

def permute(self, nums):
    result = []
    bucket = []
    def bt(arr):
        if len(arr) == len(bucket):
            result.append(bucket[:])
            return
        for x in arr:
            if x not in bucket:
                bucket.append(x)
                bt(arr)
                bucket.pop()

    bt(nums)
    return result

