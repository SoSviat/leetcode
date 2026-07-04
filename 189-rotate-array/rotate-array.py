class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        i = 0 
        p2 = len(nums)-k
        res = []
        z = 0
        k = k % len(nums)

        for i in range(len(nums)):

            if k > 0:
                counter = len(nums)-k
                res.append(nums[counter])
                k -= 1
            else:
                res.append(nums[z])
                z += 1                
        
        nums[:] = res
        
        return nums
        