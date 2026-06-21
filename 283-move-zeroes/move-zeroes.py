class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        slow = fast = 0

        ar_size = len(nums)

        while fast < ar_size:
            while slow < fast and nums[slow] != 0:
                slow += 1

            if slow < fast:
                nums[slow], nums[fast] = nums[fast], nums[slow]

            fast += 1
            
        #O(n)
        #O(1)