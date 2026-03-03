class Solution:
    def isPalindrome(self, x: int) -> bool:
        str1 = str(x)
        if(str1[0] == "-"):
            return False

        lengStr = len(str1)
        for i in range(lengStr):
            if(str1[i] != str1[lengStr - 1 - i]):
                return False
        return True