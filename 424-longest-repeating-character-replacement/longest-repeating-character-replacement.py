class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dict_ = {}
        best = left = window_size = 0

        for right in range(len(s)):
            if s[right] in dict_:
                dict_[s[right]] += 1
            else:
                dict_[s[right]] = 1


            max_letter = max(dict_.values()) 
            window_size = right - left +1

            if window_size - max_letter > k:
                dict_[s[left]] -= 1
                left += 1
            
            window_size = right - left +1
            
            best = max(best, window_size)
            
    
        return best
        
        #O(n)
        #O(1)
