class Solution:
    def makeGood(self, s: str) -> str:
        
        res = ''

        for i in range(len(s)):
            #if res and s[i].isupper() and res[-1].upper() == s[i]:
            #   res = res[:-1]
            #elif res and s[i].islower() and res[-1] == s[i].upper():
            #   res = res[:-1]
            if res and (
                (s[i].isupper() and res[-1].upper() == s[i] and res[-1].islower()) or
                (s[i].islower() and res[-1] == s[i].upper() and res[-1].isupper())
            ):
                res = res[:-1]
            else:
                res += s[i]


        return res