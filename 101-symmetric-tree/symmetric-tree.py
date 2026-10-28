# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode | None) -> bool:
        
        res = True

        def dfs(left, right):
            nonlocal res

            if not left and not right:
                #res = True
                return True
            if not left and right or not right and left:
                res = False
                return False

            if(left.val == right.val):
                dfs(left.left, right.right)
                dfs(left.right, right.left)

                if left.val != right.val:
                    res = False
                    return res
            else:
                res = False
                return False

            return res

        return dfs(root.left, root.right)
