class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        
        nums_hash = {}
        counter = 0

        for i in range(len(nums)):
            
            if nums[i] in nums_hash:
                counter += nums_hash[nums[i]]
                nums_hash[nums[i]] += 1
            else:
                nums_hash[nums[i]] = 1
        
        return counter

        #O(n)
        #O(n)