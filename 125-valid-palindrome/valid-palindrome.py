class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(c.lower() for c in s if c.isalnum())
        
        i = 0
        lenght_s = len(s)
        for i in range(lenght_s):
            if(s[i] != s[lenght_s - 1 - i]):
                return False

        return True

        