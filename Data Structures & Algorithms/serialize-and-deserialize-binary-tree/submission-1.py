# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Codec:
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        q = [root]
        ans = []
        while q:
            curr = q.pop(0)
            if(curr.val=="#"):
                ans.append(curr.val)
                continue
            ans.append(str(curr.val))
            if curr.left:
                q.append(curr.left)
            else:
                q.append(TreeNode("#"))
            if curr.right:
                q.append(curr.right)
            else:
                q.append(TreeNode("#"))
        res = ",".join(ans)
        return res

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        data = data.strip(",#")
        values = list(map(lambda x: int(x) if x.isdigit() else x, filter(lambda x: x.isdigit() or x=="#", data.split(","))))
        n = len(values)
        if n == 0:
            return None
        root = TreeNode(values[0])
        q = [root]
        i = 1
        while i < n:
            curr = q.pop(0)
            if i < n:
                if(values[i] != "#"):
                    curr.left = TreeNode(values[i])
                    q.append(curr.left)
                i += 1
            if i < n:
                if(values[i] != "#"):
                    curr.right = TreeNode(values[i])
                    q.append(curr.right)
                i += 1
        return root
