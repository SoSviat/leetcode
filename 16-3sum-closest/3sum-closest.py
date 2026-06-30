class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
    
        nums.sort()
        old_res = nums[0] + nums[1] + nums[2]

        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1

            while left < right:
                res = nums[i] + nums[left] + nums[right]
                dif = target - res
                old_dif = target - old_res
                
                if dif == 0:
                    return res

                if dif > 0:
                    left += 1
                else:
                    right -= 1

                if abs(dif) < abs(old_dif):
                    old_res = res 
                


        return old_res
        #O(n^2)
        #O(n)

