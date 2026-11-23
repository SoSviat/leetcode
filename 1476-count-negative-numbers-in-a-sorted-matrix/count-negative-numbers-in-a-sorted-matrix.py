class Solution:
    def countNegatives(self, grid: list[list[int]]) -> int:
        
        left = 0
        len_grid_row = len(grid[0])-1
        counter_negative = 0

        def find_negative(l, r, i):
            while l <= r:
                mid = (l+r)//2
                if grid[i][mid] >= 0:
                    l = mid+1
                else:
                    r = mid-1
            
            res = len(grid[0]) - l

            return res

        for i in range(len(grid)):

            if grid[i][len_grid_row] < 0:
                res_counter = find_negative(left, len_grid_row, i)
                counter_negative += res_counter
        
        return counter_negative
                