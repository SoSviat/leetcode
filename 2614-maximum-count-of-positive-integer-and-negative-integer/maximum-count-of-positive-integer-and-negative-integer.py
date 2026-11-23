class Solution:
    def maximumCount(self, nums: list[int]) -> int:
        
        left = 0
        right = len(nums)-1
        def cal_negative(l, r):
            while l <= r:
                mid = (l+r)//2
                if nums[mid] >= 0:
                    r = mid-1
                elif nums[mid] < 0:
                    l = mid+1

            return r+1
        
        def cal_positive(l_p, r_p):
            while l_p <= r_p:
                mid = (l_p+r_p)//2
                if nums[mid] <=0:
                    l_p = mid+1
                else:
                    r_p = mid-1
            res = len(nums) - l_p
            return res

        

        negativs = cal_negative(left, right)

        positive = cal_positive(left, right)

        if negativs > positive:
            return negativs
        
        return positive
            