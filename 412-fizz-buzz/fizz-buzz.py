class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        
        res = []
        
        i=0 
        for i in range(n):
            i += 1
            
            res3 = i%3
            res5 = i%5

            if(res3 == 0 and res5 == 0):
                i = 'FizzBuzz'
            elif (res3 == 0):
                i = 'Fizz'
            elif (res5 == 0):
                i = 'Buzz'
               
            i = str(i)
            res.append(i)
        return res        