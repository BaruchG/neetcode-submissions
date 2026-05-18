class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]*len(nums)
        postfix = [1]*len(nums)
        product = [1]*len(nums)

        for i, value in enumerate(nums):
            if i == 0:
                prefix[i] *= 1
            else:
                prefix[i] *= nums[i-1] * prefix[i-1]
        for i in range(len(nums) -1, -1, -1):
            print(i)
            if i == len(nums) - 1:
                postfix[i] *= 1
            else:
                postfix[i] *= nums[i+1] * postfix[i+1]            
        print(prefix)
        print(postfix)
        return [prefix[i] * postfix[i] for i in range(len(nums))]
