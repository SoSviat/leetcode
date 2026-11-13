class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        def b_search(left, right):
            mid = (left + right)//2

            if left > right:
                return -1

            if nums[mid] == target:
                return mid
            
            if nums[left] <= nums[mid]:
                if target >= nums[left] and target < nums[mid]:
                    return b_search(left, mid-1)
                else:
                    return b_search(mid+1, right)
            else:
                if target <= nums[right] and target > nums[mid]:
                    return b_search(mid+1, right)
                else:
                    return b_search(left, mid-1)
            return -1

        return b_search(left, right)