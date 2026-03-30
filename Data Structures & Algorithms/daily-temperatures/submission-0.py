class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)
        for idx, i in enumerate(temperatures):

            while stack and stack[-1][0] < i:
                pos = stack[-1][1]
                days = idx - pos
                result[pos] = days
                stack.pop()

            stack.append((i, idx))

        return result 