class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        
        max = 0

        for i in accounts:
            sum_el = sum(i)
            if(sum_el > max):
                max = sum_el
        
        return max