class Solution:
    def minimumOperations(self, nums: list[int]) -> int:

        sete = set(nums)

        if( 0 in sete):
            return len(sete)-1
        
        return len(sete)