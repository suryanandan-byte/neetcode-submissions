# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def helper(root,val,m):
            if root==None:
                return 0
            l=helper(root.left,val,max(m,root.val))
            r=helper(root.right,val,max(m,root.val))
            if root.val>=m:
                return l+r+1
            return l+r
        x=helper(root.left,root.val,root.val)
        y=helper(root.right,root.val,root.val)
        return x+y+1
