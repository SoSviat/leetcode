class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        set_ = set()
        counter = 0
        
        for x in s:

            if x in set_:
                set_.remove(x)
                counter = counter + 2
            else:
                set_.add(x)
        
        if set_:
            return counter + 1
        
        return counter