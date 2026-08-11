class Solution:
    def isValid(self, s: str) -> bool:
        
        open_brackets = ["(","[","{"]

        res = []
        for i in range(len(s)):
            print(s[i])
            if s[i] in open_brackets:
                res.append(s[i])
            elif len(res) > 0:
                if s[i] == ")" and res[-1] == "(":
                    res.pop()
                elif s[i] == "]" and res[-1] == "[":
                    res.pop()
                elif s[i] == "}" and res[-1] == "{":
                    res.pop()
                else:
                    return False
            else:
                return False
            
        
        if len(res) > 0:
            return False
        
        return True