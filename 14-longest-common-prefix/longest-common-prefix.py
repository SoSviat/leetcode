class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        shortest = len(min(strs, key=len))

        str_s = strs[0]
        result = str_s[:shortest]

        if(len(strs) == 1):
            return strs[0]

        for j in range(shortest):
            for i in range(len(strs)):

   
                if(shortest < j):
                    continue

                if(result[j] != strs[i][j]):
                    return result[:j]

        return result