class Solution:
    def maxArea(self, height: List[int]) -> int:

        left = weight = result = 0
        all_blocks = right = len(height)-1
        
        while left < right:
            if height[left] > height[right]:
                weight = height[right]*all_blocks
                right -= 1
            else:
                weight = height[left]*all_blocks
                left += 1

            result = max(result, weight)
            all_blocks -= 1

        return result
        