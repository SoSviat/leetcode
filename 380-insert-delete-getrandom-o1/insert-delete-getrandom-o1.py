import random

class RandomizedSet:

    def __init__(self):
        self.random = []  
        self.quick_search = {}
        

    def insert(self, val: int) -> bool:

        if val in self.quick_search: 
            return False
        
        self.random.append(val)
        self.quick_search[val] = len(self.random) - 1
        
        return True
    
    def remove(self, val: int) -> bool:

        if val not in self.quick_search: 
            return False
        
        indx = self.quick_search[val]
        last = self.random[-1]
        
        self.random[indx] = last
        self.quick_search[last] = indx
        
        self.random.pop()
        self.quick_search.pop(val)
        
        return True

    def getRandom(self) -> int:
        return random.choice(self.random)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()