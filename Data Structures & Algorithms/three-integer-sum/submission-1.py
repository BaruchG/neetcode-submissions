class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        s = sorted(nums)
        triplets = []
        for i in range(0, len(s) -2):
            l = i + 1
            r = len(nums) - 1
            while l < r:
                total = s[i] + s[l] + s[r]
                if total == 0:
                    y = [s[i], s[l], s[r]]
                    if y not in triplets:
                        triplets.append(y)
                    l += 1
                    r -= 1
                elif total < 0:
                    l += 1
                elif total > 0:
                    r -= 1
        return triplets