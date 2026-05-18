class Solution:
    def fillCups(self, amount: List[int]) -> int:

        h = []

        for i in range(len(amount)):
            heapq.heappush(h, -amount[i])
       
        counter = 0

        while h:
            top1 = heapq.heappop(h)
            top2 = heapq.heappop(h)
            
            if top1 == 0:
                break
 
            heapq.heappush(h, top1+1)
            heapq.heappush(h, top2+1)
            counter += 1
           
        # print(counter)
        return counter