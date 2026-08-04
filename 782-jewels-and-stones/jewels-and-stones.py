class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        
        counter = 0
        
        for i in range(len(stones)):
            if stones[i] in jewels:
                counter += 1
        
        return counter

        #O(1)
        #O(1)