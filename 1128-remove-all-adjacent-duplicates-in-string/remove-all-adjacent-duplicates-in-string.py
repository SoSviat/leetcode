class Solution:
    def removeDuplicates(self, s: str) -> str:
        
        res = ''
        for i in range(len(s)):
            if not res or res[-1] != s[i]:
                res = res + s[i]
            else:
                res = res[:-1]
        return res