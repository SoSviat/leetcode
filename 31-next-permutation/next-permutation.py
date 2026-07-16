class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        end = len(nums)-1
        pre_end = end -1
        change_indx = -1

        for i in range(len(nums)):
            if nums[end] > nums[pre_end]:
                change_indx = pre_end
                end2 = len(nums) - 1
                while nums[change_indx] >= nums[end2]:
                        end2 -= 1
                nums[change_indx], nums[end2] = nums[end2], nums[change_indx]
                break
            else:
                pre_end -= 1
                if pre_end >= 0:
                    end -=1
                else:
                    break

        right = len(nums)-1
        left = change_indx+1

        while left <= right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

        #O(n)
        #O(1)