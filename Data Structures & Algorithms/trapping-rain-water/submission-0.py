class Solution:
    def trap(self, height: List[int]) -> int:
        result = 0
        left_max = [0]
        right_max = [0] * (len(height) + 1)
        for h in height: 
            left_max.append(max(left_max[-1], h))
        for h in range(len(height) - 1, -1,-1): 
            right_max[h] = max(right_max[h+1], height[h])
        for h in range(len(height)): 
                result += min(left_max[h+1],right_max[h]) - height[h]
        return result 