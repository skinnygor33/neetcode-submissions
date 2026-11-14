class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set()
        lenght = 0
        for num in nums: 
            seen.add(num)
        for num in seen: 
            if num - 1 not in seen: 
                current = num 
                current_length = 1
                while current + 1 in seen: 
                    current_length += 1
                    current += 1
                lenght = max(lenght, current_length)
        return lenght
        """
        nums = [2,20,4,10,3,4,5]
                     i



        seen = {2:[2], 20:[20], 10:[10]}

        """