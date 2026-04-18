class Solution:
    def fib(self, n: int, dict_: list | None = None) -> int:
        
        #print('start')
        #res = n 
        if n == 0 or n == 1:
            return n
            
        if dict_ is None:
            dict_ = []
            dict_.append(0)
            dict_.append(1)
    

        if len(dict_) == n:
            #print('win 1')
            res = dict_[-1] + dict_[-2]
            #print(res)
            return res
        else:
            #print('append')
            dict_.append(dict_[-1] + dict_[-2])
            self.fib(n, dict_)

        #print(dict_)

        #print('final?', res)
        return self.fib(n, dict_)
        #return n

        #if(n == 0 or n == 1):
        #    return n
        #            
        #res = self.fib(n - 1, dict_) + self.fib(n - 2, dict_)
        #return res