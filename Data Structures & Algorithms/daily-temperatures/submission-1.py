class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0]*len(temperatures)

        for i, currTemp in enumerate(temperatures):
            while stack and stack[-1][1] < currTemp:
                oldIndex, temp = stack.pop()
                res[oldIndex] = i - oldIndex
            stack.append((i, currTemp))
        return res