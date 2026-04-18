class Solution:
    def climbStairs(self, n: int, dict_:list | None = None) -> int:

        if n == 1 or n == 2:
            return n

        if dict_ is None:
            dict_ = []
            dict_.append(1)
            dict_.append(2)
        
        res = dict_[-1] + dict_[-2]

       # print(len(dict_))
        #counter_ += 1
        #print(counter_)
        if len(dict_) == n-1:
            return res
        else:
            dict_.append(res)
            return self.climbStairs(n, dict_)
