class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
    
        dict_1 = {}
        dict_2 = {}

        for i in range(len(s)):
            
            if s[i] in dict_1:
                if dict_1[s[i]] != t[i]:
                    return False
            else:
                dict_1[s[i]] = t[i]


            if t[i] in dict_2:
                if dict_2[t[i]] != s[i]:
                    return False
            else:
                dict_2[t[i]] = s[i]
        
        return True

        #O(n)
        #O(1)