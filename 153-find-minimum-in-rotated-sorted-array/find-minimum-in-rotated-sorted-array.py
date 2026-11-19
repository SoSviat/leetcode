class Solution:
    def findMin(self, nums: list[int]) -> int:
        
        left = 0
        right = len(nums)-1

        while left < right:
            mid = (left+right)//2
            
            if nums[right] < nums[mid]:
                left = mid+1
            else:
                right = mid

        return nums[left]

        # for i in range(len(nums)):
        #     if i > 0:
        #         if nums[i] < nums[i-1]:
        #             return nums[i]


        # return nums[0]