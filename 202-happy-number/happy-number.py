class Solution:
    def isHappy(self, n: int) -> bool:
        
        number_hash = set()

        while n !=1:
            
            if n in number_hash:
                return False
            else:
                number_hash.add(n)

                n_str = str(n)
                new_n = 0
                
                for i in n_str:
                    new_n += int(i)*int(i)
                
                n = new_n


        return True
            