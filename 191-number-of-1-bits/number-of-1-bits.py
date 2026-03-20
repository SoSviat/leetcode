class Solution:
    def hammingWeight(self, n: int) -> int:
    
        res = ''
        while n > 0:
            if(n % 2 or n == 1):
                res += '1'
            else:
                res += '0'

            n = int(n /2)
    
        j = 0
        for i in range(len(res)):
            if(res[i] == '1'):
                j = j+1

        return j