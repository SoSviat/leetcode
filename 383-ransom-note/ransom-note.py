class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
    
        colection = {}

        for i in range(len(magazine)):
            
            if magazine[i] in colection:
                colection[magazine[i]] += 1
            else:
                colection[magazine[i]] = 1
       
        for i in range(len(ransomNote)):
            
            if ransomNote[i] in colection and colection[ransomNote[i]] > 0:
                colection[ransomNote[i]] -= 1
            else:
                return False
        
        return True

        #O(N)
        #O(1)