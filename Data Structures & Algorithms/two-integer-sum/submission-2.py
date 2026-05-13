class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {} #val, index
        for i, val in enumerate(nums):
            diff = target - val
            if diff in hm:
                return [hm[diff], i]
            else:
                hm[val] = i