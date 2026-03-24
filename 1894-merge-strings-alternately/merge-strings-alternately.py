class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        res = ''
        long_word = word1
        short_word = word2
        
        if(len(word1) < len(word2)):
            long_word = word2
            short_word = word1

        for i in range(len(long_word)):
            if(i  < len(word1)):
                res += word1[i]
            
            if(i  < len(word2)):
                res += word2[i]
          

        return(res)