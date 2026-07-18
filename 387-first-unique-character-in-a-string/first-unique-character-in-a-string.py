class Solution:
    def firstUniqChar(self, s: str) -> int:
        chart_hash = defaultdict(int)

        for c in s:
            chart_hash[c] += 1
        
        for i, v in enumerate(s):
            if v in chart_hash and chart_hash[v] == 1:
                return i
        return -1

        #O(n)
        #O(1)