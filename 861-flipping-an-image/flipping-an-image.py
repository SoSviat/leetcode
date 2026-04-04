class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:

        res = []
        
        for i in range(len(image)):
            res.append([])
            for j in range(len(image[i])):
                val = 1
                if(image[i][j] == 1):
                    val = 0
                res[i].insert(0, val)

        return(res)