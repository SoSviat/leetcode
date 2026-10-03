class Solution:
    def minimumOperations(self, nums: list[int]) -> int:

        heap = []
        for i in range(len(nums)):
            heapq.heappush(heap, nums[i])


        countter = 0 
        current = 0

        while heap:
            
            heap_head = heapq.heappop(heap)

            if current != heap_head:
                countter += 1
                current = heap_head


        return countter
    


        # sete = set(nums)

        # if( 0 in sete):
        #     return len(sete)-1
        
        # return len(sete)