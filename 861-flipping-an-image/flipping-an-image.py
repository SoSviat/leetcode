class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:

        res = []
       # val = 0
        for i in range(len(image)):
            #print(image[i])
            res.append([])
            for j in range(len(image[i])):
                val = 1
                if(image[i][j] == 1):
                    val = 0
                #print(image[i][j], ' = ' , 1, 'val - ', val)
                #res[i].insert(0, image[i][j])
                res[i].insert(0, val)

        return(res)