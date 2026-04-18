class Solution:
    def fib(self, n: int, dict_: list | None = None) -> int:
        
        if n == 0 or n == 1:
            return n

        if dict_ is None:
            dict_ = []
            dict_.append(0)
            dict_.append(1)
    
        res = dict_[-1] + dict_[-2]

        if len(dict_) == n:
            return res
        else:
            dict_.append(res)
            self.fib(n, dict_)

        return self.fib(n, dict_)
        
        #O(n)
        #O(n)


        #if(n == 0 or n == 1):
        #    return n
        #            
        #res = self.fib(n - 1, dict_) + self.fib(n - 2, dict_)
        #return res
        #O(2**n)
        #O(n)