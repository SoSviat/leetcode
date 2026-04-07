class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        step = 0
        res = 0
        for i in range(len(nums)):
            if(nums[i] == val):
                step += 1
            else:
                res +=1
                nums[i-step] = nums[i]

        return res