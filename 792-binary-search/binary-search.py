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

            if target < nums[mid]:
                return b_search(left, mid-1)
            else: 
                return b_search(mid+1, right)

            return -1

        return b_search(left, right)

        # i = 0

        # for num in nums:
        #     if num == target:
        #         return i

        #     if target < num: 
        #         return -1

        #     i += 1 