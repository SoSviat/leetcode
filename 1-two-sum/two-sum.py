class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        dict_ = {}
    
        for i, num in enumerate(nums):
            rest_target = target - num
    
            if rest_target in dict_:
                return [dict_[rest_target], i]
            
            dict_[num] = i

        #0(n2)
        #0(1)

    #    for i in range(len(nums)):
    #        for j in range(i + 1, len(nums)):
    #            if nums[i] + nums[j] == target:
    #                return [i, j]
    

     #0(n)
     #0(1)