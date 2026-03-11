class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        
        i=0
        pre_sum=0

        res = []
        for i in range(len(nums)):

            if(i == 0):
                res.append(nums[i])
                pre_sum = nums[i]
            else:
                pre_sum += nums[i]
                res.append(pre_sum)

        return res
