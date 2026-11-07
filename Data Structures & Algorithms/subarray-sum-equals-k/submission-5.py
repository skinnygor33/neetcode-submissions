class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        seen = {}
        prefix = 0
        seen[prefix] = 1
        result = 0

        for i in range(len(nums)): 
            prefix += nums[i]
            needed = prefix - k
            if needed in seen: 
                result += seen[needed]
            if prefix in seen: 
                seen[prefix] += 1
            else: 
                seen[prefix] = 1
        return result 


        