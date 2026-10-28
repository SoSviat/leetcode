# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode | None) -> bool:
        
        def dfs(node):
            if not node: return 0

            left_height = dfs(node.left)
            right_height = dfs(node.right)
            
            if left_height == -1 or right_height == -1:
                return -1

            dif = left_height - right_height
            
            if  dif >= 2  or dif <= -2:
                return -1

            res = 1
            if left_height > right_height:
                return res+left_height

            return res+right_height

        if dfs(root) == -1:
            return False

        return True