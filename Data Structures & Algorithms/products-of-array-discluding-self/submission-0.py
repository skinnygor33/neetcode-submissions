class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        left = []
        right = []
        output = []
        for num in nums: 
            prefix *= num
            left.append(prefix)
        prefix = 1
        for num in range(len(nums)-1, -1, -1): 
            prefix *= nums[num]
            right.append(prefix)
        right.reverse()
        for i in range (0,len(nums)): 
            if i == len(nums) - 1:
                output.append(left[i-1])
            elif i == 0:
                output.append(right[i+1])
            else:
                output.append(left[i-1]*right[i+1])
        return output
        