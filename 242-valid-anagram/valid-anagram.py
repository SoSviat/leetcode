class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        container = {}
        lenght = len(s)

        if(lenght != len(t)):
            return False
        
        for i in range(lenght):
            if s[i] in container:
                container[s[i]] += 1
            else:
                container[s[i]] = 1

        for i in range(lenght):
            if t[i] in container and container[t[i]]>0:
                container[t[i]] -= 1
            else:
                return False
        
        return True

