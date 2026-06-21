class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        start = 0
        end = pos = len(nums)-1
        res = [0] * len(nums)

        while start <= end: 
            if(nums[start]**2 > nums[end]**2):
                res[pos] = nums[start]**2
                start += 1
            else:
                res[pos] = nums[end]**2
                end -= 1
                
            pos -= 1
        
        return res
        # for i in range(len(nums)):
        #     nums[i] = nums[i] * nums[i]

        # nums.sort()
        # return nums