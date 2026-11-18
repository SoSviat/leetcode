class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        left = 0
        right = len(matrix)-1
        
        while left <= right:
            mid = (left+right)//2
            
            if matrix[mid][0] > target:
                right = mid-1
            elif matrix[mid][-1] < target:
                left = mid+1
            else:

                row = matrix[mid]
                left_inside = 0
                right_inside = len(row) - 1

                while left_inside <= right_inside:
                    mid_inside = (left_inside + right_inside) // 2

                    if row[mid_inside] == target:
                        return True
                    elif row[mid_inside] < target:
                        left_inside = mid_inside + 1
                    else:
                        right_inside = mid_inside - 1

                return False

        return False