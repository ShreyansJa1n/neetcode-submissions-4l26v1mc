class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        for i in range(len(heights)):
            last_height = -1
            while stack and stack[-1][1] >= heights[i]:
                height_idx, height = stack.pop()
                area = (i - height_idx) * height
                max_area = max(area, max_area)
                last_height = height_idx
            
            if last_height != -1:
                stack.append((last_height, heights[i]))
            else:
                stack.append((i, heights[i]))

        while stack:
            height_idx, height = stack.pop()
            area = ((len(heights) - height_idx)) * height
            max_area = max(area, max_area)
            last_height = height_idx

        return max_area
