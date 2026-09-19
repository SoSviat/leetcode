from math import isqrt
import heapq
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        #[100, 64, 25, 9, 4]
        #[10, 8, 5, 9, 4]
        #[3, 8, 5, 9, 4]

        heap = [-gift for gift in gifts]
        heapq.heapify(heap)

        i = 0 
        while i < k:

            top = -heapq.heappop(heap)
            get_gifts = isqrt(top)
            heapq.heappush(heap, -get_gifts)
            i = i +1

        all_gift = sum(heap)

        return all_gift* (-1)

# O(N log N)
# O(N )