class Solution:
    def findMin(self, nums: list[int]) -> int:
        print(nums)

        for i in range(len(nums)):
            if i > 0:
                if nums[i] < nums[i-1]:
                    return nums[i]


        return nums[0]