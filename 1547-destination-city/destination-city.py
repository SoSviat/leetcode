class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        departure = set()

        for i in range(len(paths)):
            departure.add(paths[i][0])

        for i in range(len(paths)):
            if paths[i][1] not in departure:
                return paths[i][1]

        #O(n)
        #O(n)