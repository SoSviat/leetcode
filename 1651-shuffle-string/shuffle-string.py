class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        res = {}
        sorted_items = ''
        finish = ''
        for i in range(len(s)):
            res[indices[i]] = s[i]

        sorted_items = sorted(res.items())

        for i in range(len(s)):
            finish += sorted_items[i][1]

        return(finish)