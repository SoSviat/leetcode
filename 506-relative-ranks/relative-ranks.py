class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        res = []

        score = sorted(enumerate(score), key=lambda x: x[1], reverse=True)        
        res = [''] * len(score)

        for rank, (i, s) in enumerate(score):
            if rank == 0:
                res[i] = "Gold Medal"
            elif rank == 1:
                res[i] = "Silver Medal"
            elif rank == 2:
                res[i] = "Bronze Medal"
            else:
                res[i] = str(rank+1)

        return res
        
        #O(nlogn)
        #0(n)
        
