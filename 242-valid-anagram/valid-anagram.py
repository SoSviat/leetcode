class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        dic_ = {}
        
        for i in s:
            if i in dic_:
                dic_[i] = dic_[i] + 1
            else:
                dic_[i] = 1

        for i in t:
            if i not in dic_:
                return False

            dic_[i] -= 1

            if dic_[i] == 0:
                del dic_[i]
            
        return True

        #0(n)
        #0(1)