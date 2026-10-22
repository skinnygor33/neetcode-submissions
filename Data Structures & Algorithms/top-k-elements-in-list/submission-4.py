import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        for i in nums: 
            frequency[i] = frequency.get(i,0) + 1
        heap = []
        track = 0

        for element, number in frequency.items():
            heapq.heappush(heap, (number,element))
            if len(heap) > k: 
                heapq.heappop(heap)

        return [count for element, count in heap]





        