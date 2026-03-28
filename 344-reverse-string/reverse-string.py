class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        lenght_ar = len(s)
        arr_copy = s.copy()
        i = 0
   
        while lenght_ar != 0:
            s[i] = arr_copy[lenght_ar-1]
            lenght_ar -= 1
            i += 1