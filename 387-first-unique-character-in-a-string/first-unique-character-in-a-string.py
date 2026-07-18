class Solution:
    def firstUniqChar(self, s: str) -> int:
        chart_hash = defaultdict(int)
        #print(s)

        for c in s:
            chart_hash[c] += 1
        
        i = 0
        res = -1

        for key, val in chart_hash.items():
            #print(s[val])
            if val == 1:

                res = key
                break
            i += 1

        for i in range(len(s)):
            print(s[i],'- ', res)
            if s[i] == res:
                return i
        
        return res