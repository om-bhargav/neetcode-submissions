# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSame(p,q):
            if(not p and not q):
                return True
            if(not p or not q):
                return False
            if p.val!=q.val:
                return False
            return isSame(p.left,q.left) and isSame(p.right,q.right)
        ans = False
        def dfs(root):
            nonlocal ans
            if not root:
                return None
            if root.val==subRoot.val and not ans:
               ans = isSame(root,subRoot)
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return ans