import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        result = []
        for i in range(len(nums)): 
            frequency[nums[i]] = frequency.get(nums[i],0) + 1
        heap = []
        for number,times in frequency.items(): 
            heap.append([times,number])
        heapq.heapify(heap)
        counter = len(heap)
        while counter > k: 
            heapq.heappop(heap)
            counter -= 1
        
        for time,number in heap: 
            result.append(number)
        return result
