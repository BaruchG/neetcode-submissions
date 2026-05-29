class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left_pointer = 0
        right_pointer = len(nums) -1
        while left_pointer <= right_pointer:
            half = left_pointer + int((right_pointer-left_pointer)/2)
            if nums[half] < target:
                left_pointer = half + 1
            elif nums[half] > target:
                right_pointer = half - 1
            elif nums[half] == target:
                return half
        return -1