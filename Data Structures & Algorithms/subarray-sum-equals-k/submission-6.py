class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        seen = {0:1}
        prefix = 0
        result = 0
        for i in range(len(nums)): 
            prefix += nums[i]
            needed = prefix - k
            if needed in seen: 
                result += seen[needed]
            seen[prefix] = seen.get(prefix,0) + 1
        return result