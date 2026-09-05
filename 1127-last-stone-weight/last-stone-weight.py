import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        heap = []
        for i in range(len(stones)):
            heap.append(-stones[i])

        heapq.heapify(heap)

        while len(heap) > 1:
            first = heapq.heappop(heap)
            first = -first

            second = heapq.heappop(heap)
            second = -second

            if first != second:
                difference = first - second
                heapq.heappush(heap, -difference)

        if len(heap) > 0:
            result = -heap[0]
            return result
        else:
            return 0

        #O(n log n)
        #O(n)