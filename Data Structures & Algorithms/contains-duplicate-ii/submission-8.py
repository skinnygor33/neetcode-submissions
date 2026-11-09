class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = {}
        for i in range(0,len(nums)):
            if nums[i] in seen: 
                if abs(i - seen.get(nums[i])) <= k: 
                    return True
                seen[nums[i]] = i
            else: 
                seen[nums[i]] = i
        return False
        