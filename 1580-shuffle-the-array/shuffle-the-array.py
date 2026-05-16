class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        
       # print(nums)
      #  print(n)
        
        res = []

        for i in range(len(nums)):
            
            if(len(nums)-(i+n) >0):
                print(i)
                res.append(nums[i])
                res.append(nums[i+n])
        
      #  print(res)
        return res
