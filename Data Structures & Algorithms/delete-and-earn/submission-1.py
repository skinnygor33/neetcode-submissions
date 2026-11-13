class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[-1]
        points = [0] * (max(nums) + 1)
        for i in range(len(nums)): 
            points[nums[i]] += nums[i]
        dp = [0] * len(points)
        dp[0] = points[0]
        dp[1] = max(dp[0],points[1] )
        for i in range(2, len(points)): 
            dp[i] = max(dp[i-1], dp[i-2]+points[i])
        return dp[-1]