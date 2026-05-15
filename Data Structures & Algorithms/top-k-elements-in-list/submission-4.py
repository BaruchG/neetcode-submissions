class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter

        nums = Counter(nums)
        
        nums = sorted(nums.items(), key=lambda x:x[1])
        print(nums)

        solution = []
        for i in range(0, k):
            solution.append(nums[-1-i][0])
        return solution
        