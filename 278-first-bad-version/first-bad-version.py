# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        
        left = 1
        right = n

        def b_search(left, right):
            mid = (left + right)//2

            if left > right:
                return 1

            if isBadVersion(mid) == False and isBadVersion(mid+1) == True:
                return mid+1


            if isBadVersion(mid) == True:
                return b_search(left, mid-1)
            elif isBadVersion(mid) == False:
                return b_search(mid+1, right)

            return 1

        return b_search(left, right)

    

        # while n:  
        #     if isBadVersion(n) == False:
        #         return n+1

        #     if n == 1:
        #         return 1
            
        #     n -= 1

        # return n