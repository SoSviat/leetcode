class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        res = 0
        best = - 99999999999

        for i in range(len(nums)):
            res += nums[i]

            if i >= k:
                res -= nums[i-k]
            
            if i >= k-1:
                best = max(best, res)
            
            
        
        return best/k   

        #O(n)
        #O(1)
