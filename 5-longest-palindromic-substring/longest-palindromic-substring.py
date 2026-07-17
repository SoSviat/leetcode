class Solution:
    def longestPalindrome(self, s: str) -> str:

        best = s[0]

        for i in range(len(s)):

            best1 = self.checkPallindrome(s, i, i)
            best2 = self.checkPallindrome(s, i, i+1)

            if len(best1) > len(best2):
                top_best = best1
            else:
                top_best = best2

            if len(top_best) > len(best):
                best = top_best

        return best

    def checkPallindrome(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        
        return s[left+1:right]

    #O(n^2)
    #O(1)