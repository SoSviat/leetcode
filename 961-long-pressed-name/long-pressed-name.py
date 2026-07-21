class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        
        p1 = p2 = 0

        while p2 < len(typed):
            
            if p1 < len(name) and name[p1] == typed[p2]:
                p2 += 1
                p1 += 1
            elif p2 > 0 and typed[p2] == typed[p2-1]:
                p2 += 1
            else:
                return False
        
        if p1 < len(name):
            return False
            
        return True