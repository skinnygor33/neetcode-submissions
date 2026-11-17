class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        seen = set()
        nums.sort()
        left = 0
        right = len(nums) - 1
        result = []
        current = ()
        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1
            while left < right: 
                if nums[left] + nums[right] == -1 * nums[i]: 
                    current = (nums[i], nums[left], nums[right])
                    if current not in seen:
                        result.append([nums[i], nums[left], nums[right]])
                        seen.add(current)
                        left += 1
                        right -= 1
                    else:
                        left += 1
                        right -= 1
                elif nums[left] + nums[right] > -1 * nums[i]: 
                    right -= 1
                else:
                    left += 1
        return result
        