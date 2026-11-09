class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        best = 0
        start = 0
        for x in s: 
            if x - 1 in s: 
                pass
            else: 
                start = x
                lenght = 1
                while x + 1 in s: 
                    lenght += 1
                    x += 1
                best = max(best, lenght)
        return best



