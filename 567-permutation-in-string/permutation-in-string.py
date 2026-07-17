class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dict_ = {}
        for i in range(len(s1)):
            if s1[i] in dict_:
                dict_[s1[i]] +=1
            else:
                dict_[s1[i]] = 1
        

        dict_2 = {}
        for i in range(len(s2)):
            if s2[i] in dict_2:
                dict_2[s2[i]] +=1
            else:
                dict_2[s2[i]] = 1

            if i >= len(s1):
                left_char = s2[i - len(s1)] 
                dict_2[left_char] -= 1 
                
                if dict_2[left_char]  == 0:
                    del dict_2[left_char]

            if i >= len(s1)-1:
                if dict_ == dict_2:
                    return True
        
        return False
    
        # O(m+n)
        # O(1)