class Solution:
    def isValid(self, s: str) -> bool:
        
      #  print(s)

        if(int(len(s)) % 2 != 0):
            return False

        res = []
        pos = 'start'
        close = [')', ']', '}']

        for i in range(len(s)):
            if s[i] in close:
                if(
                    (s[i] == ')' and len(res) and res[-1] == '(') or
                    (s[i] == ']' and len(res) and res[-1] == '[') or
                    (s[i] == '}' and len(res) and res[-1] == '{')
                ):
                    res.pop()
                else:
                    return False
            else:
                res.append(s[i])
        
        if(len(res)):
            return False

        return True
            