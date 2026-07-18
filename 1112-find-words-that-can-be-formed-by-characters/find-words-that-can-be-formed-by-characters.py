class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        
        dict_ = {}
        res = 0

        for i in range(len(chars)):
            if chars[i] in dict_:
                dict_[chars[i]] += 1
            else:
                dict_[chars[i]] = 1

        #print(dict_)
        flag = 0
        for word in words:
            
            chart_hash = {}
            for letter in word:
                if letter in chart_hash:
                    chart_hash[letter] += 1
                else:
                    chart_hash[letter] = 1

            flag = 0
            for key, value in chart_hash.items():
                if key not in dict_ or chart_hash[key] > dict_[key]:
                    flag = 1
            
            if flag == 0:
                res += len(word)
            
        print(res)
        return(res)

        #O(n+m)
        #O(1)