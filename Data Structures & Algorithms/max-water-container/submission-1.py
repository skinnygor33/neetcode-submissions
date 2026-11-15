class Solution:
    def maxArea(self, heights: List[int]) -> int:
        globalMax = 0
        start = 0
        end = len(heights) - 1
        h = 0
        while (start < end): 
            w = abs(end - start)
            if heights[end] > heights[start]: 
                h = heights[start]
            elif heights[end] < heights[start]:
                h = heights[end]
            else: 
                h = heights[end]
            a = w * h 
            if a > globalMax:
                globalMax = a
            if heights[start] > heights[end]:
                end -= 1
            else: 
                start += 1
        return globalMax