class Solution:
    def mySqrt(self, x: int) -> int:
        
        i = 0
        r = x
        while i <= r:
            mid = (i+r)//2
            
            sqrt_ = mid*mid
            if sqrt_ > x:            
                r = mid-1
            else:
                i = mid+1
            
        return r