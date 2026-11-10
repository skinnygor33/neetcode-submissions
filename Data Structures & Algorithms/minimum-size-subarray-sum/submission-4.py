class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        p1 = 0
        p2 = 0 
        result = len(nums)

        while p2 < len(nums): 
            if sum(nums[p1:p2+1]) >= target:
                result = min(result, len(nums[p1:p2+1]))
                p1 += 1
            else:
                p2 += 1
        
        if result == len(nums): 
            if sum(nums) >= target: 
                return result 
            else:
                return 0
        return result 