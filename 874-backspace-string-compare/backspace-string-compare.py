class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        res_s = ''
        res_t = ''

        for i in range(len(s)):
            if s[i] == '#':
                res_s = res_s[:-1]
            else:
                res_s += s[i]

        for i in range(len(t)):
            if t[i] == '#':
                res_t = res_t[:-1]
            else:
                res_t += t[i]

        return res_s == res_t