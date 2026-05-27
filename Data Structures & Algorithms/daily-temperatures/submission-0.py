class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # result = [-1] * len(temperatures)
        warmest = [0] * len(temperatures)
        stack = []
        for i, num in enumerate(temperatures):
            print("stack ", stack)
            # print("result ", result)
            print("num ", num)
            print("i ", i)
            print("warmest ", warmest)
            while stack and temperatures[stack[-1]] < num:
                print("in while")
                prev_i  = stack.pop()
                # result[prev_i] = num
                warmest[prev_i] = i - prev_i
            stack.append(i)

        return warmest