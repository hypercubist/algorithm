# two sum
# 여러 방법 중 해시테이블을 이용한 방법
# 키+값 = target, 

def twoSum(self, nums, target):
    ht = {}
    results = []
    for i in range(len(nums)):
        if nums[i] in ht:
            results.append(i)
            results.append(ht[nums[i]][1])
        else:
            ht[target - nums[i]] = [nums[i], i] #해시테이블 구성 핵심포인트

    return results