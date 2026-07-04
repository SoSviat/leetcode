class Solution:
    def findLucky(self, arr: List[int]) -> int:
        
        _dict = {}
        lucky_int = -1

        for i in range(len(arr)):
            if arr[i] in _dict:
                _dict[arr[i]] = _dict[arr[i]] + 1
            else:
                _dict[arr[i]] = 1

        for key, value in _dict.items():
            if key == value and key > lucky_int:
                lucky_int = key
            

        return lucky_int
        
        #O(n)
        #O(n)