class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
        i = (len(nums) // 2) - 1
        if nums[i] == target: 
            return i 
        elif nums[i] < target:
            result = self.search(nums[i+1:], target)
            if result == -1:
                return -1
            return result + i + 1
        else: 
            return self.search(nums[:i+1], target)  