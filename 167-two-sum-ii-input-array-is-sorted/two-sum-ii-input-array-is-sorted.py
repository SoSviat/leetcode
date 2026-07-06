class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        left = 0 
        right = len(nums)-1

        while left < right:

            sum_ar = nums[left]+nums[right]
            
            if sum_ar == target:
                return [left+1, right+1]
            elif sum_ar > target:
                right -= 1
            else:
                left += 1
        
