class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left_pointer = 0
        right_pointer = len(nums) - 1
        

        while left_pointer <= right_pointer:
            mid = left_pointer + (right_pointer - left_pointer) // 2
            if nums[mid] == target:
                return mid
            if nums[left_pointer] <= nums[mid]:
                if (target <= nums[mid] and target >= nums[left_pointer]):
                    right_pointer = mid -1
                else:
                    left_pointer = mid + 1
            else:
                if (target >= nums[mid] and target <= nums[right_pointer]):
                    left_pointer = mid + 1
                else:
                    right_pointer = mid - 1
        return -1
            