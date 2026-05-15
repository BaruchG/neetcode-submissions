class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = ["x"]*len(nums)

        print(output)

        for i, value in enumerate(nums):
            for j, value2 in enumerate(output):
                if value2 == 'x' and i != j:
                    output[j] = value
                elif i != j:
                    output[j] *= value
        return output
