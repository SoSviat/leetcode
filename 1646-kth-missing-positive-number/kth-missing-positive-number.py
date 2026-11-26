class Solution:
    def findKthPositive(self, arr: list[int], k: int) -> int:
        

        dict_ = []
        print(arr)
        print(k)
        j = 0
        i = 1  
        while len(dict_) <= k:


            if  j >= len(arr) or i < arr[j]:
                dict_.append(i)
                if len(dict_) == k:
                    return i
            else:
                j +=1

            i += 1


        if len(dict_) < k:
            diff = k - len(dict_)
            if dict_[-1] > arr[-1]:
                max_val = dict_[-1]
            else:
                max_val = arr[-1]
                
            return max_val + diff

        print(dict_)