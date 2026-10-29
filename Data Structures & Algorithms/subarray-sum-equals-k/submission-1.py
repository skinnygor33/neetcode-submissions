class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        seen = {0: 1}          # the prefix "0" before any number: seen once
        total = 0
        result = 0
        for num in nums:
            total += num                      
            needed = total - k                      
            result += seen.get(needed, 0)         
            seen[total] = seen.get(total, 0) + 1 
        return result
        
