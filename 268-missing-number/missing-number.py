class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # 1 find the expected sum = 6 
        # 1 current sum = 4 
        # 1 expected sum - currect sum = 4 -6 
        
        exected_sum = ((len(nums)+1) * len(nums))//2
        #print(exected_sum)

        sum_nums = sum(nums)
        #print(sum_nums)
        return exected_sum - sum_nums

        #nums.sort() 

        #for i in range(len(nums)):
         #   if i != nums[i]:
          #      return i

        #return len(nums)

        # O(N long N)
        # O(N)