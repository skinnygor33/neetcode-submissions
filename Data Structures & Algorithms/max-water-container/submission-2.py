class Solution:
    def maxArea(self, heights: List[int]) -> int:
        globalMax = 0
        s = 0
        end = len(heights) - 1
        h = 0
        while (s < end): 
            w = abs(end - s)
            if heights[end] > heights[s]: 
                h = heights[s]
            elif heights[end] < heights[s]:
                h = heights[end]
            else: 
                h = heights[end]
            a = w * h 
            if a > globalMax:
                globalMax = a
            if heights[s] > heights[end]:
                end -= 1
            else: 
                s += 1
        return globalMax