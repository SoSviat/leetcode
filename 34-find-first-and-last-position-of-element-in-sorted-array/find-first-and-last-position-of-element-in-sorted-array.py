class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        
        def searchLeft(left, right):
            while left <= right:            
                mid = (left + right)//2

                if nums[mid] == target:
                    if mid == 0:
                        return mid
                    if nums[mid-1] == target:
                        right = mid -1
                    else:
                        return mid
                elif nums[mid] <= target:
                    left = mid +1
                else:
                    right = mid-1
                
            return -1

        def searchRight(left, right):
            while left <= right:            
                mid = (left + right)//2

                if nums[mid] == target:
                    if mid == len(nums)-1:
                        return mid
                    if nums[mid+1] == target:
                        left = mid +1
                    else:
                        return mid
                elif nums[mid] <= target:
                    left = mid +1
                else:
                    right = mid-1
                
            return -1

        res = []
        left = 0 
        right = len(nums)-1

        left_s = searchLeft(left, right)
        right_s = searchRight(left, right)

        res.append(left_s)
        res.append(right_s)
        return res