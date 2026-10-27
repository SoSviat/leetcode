# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        res = True

        def dfs(p,q):
            nonlocal res
            if (not p and q) or (not q and p):
                res = False
                return res

            if p and q:
                if p.val != q.val:
                    res = False
                    return res

                dfs(p.left, q.left)
                dfs(p.right, q.right)
            
            return res

        res = dfs(p,q)
        return res
        #0(n)
        #0(n)