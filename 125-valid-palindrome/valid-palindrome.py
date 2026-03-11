class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = ""

        for c in s:
            if c.isalnum():
                result += c.lower()

        s = result
        
        i = 0
        lenght_s = len(s)
        for i in range(lenght_s):
            if(s[i] != s[lenght_s - 1 - i]):
                return False

        return True

        