class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        print(nums)
        
        nums.sort()

        for i in range(len(nums)):
            print(i)
            if i != nums[i]:
                return i

        return len(nums)