# ACCEPTED

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def dfs(node, arg):
            if not node:
                return 0

            if not node.left and not node.right:
                if arg == "left":
                    return node.val
                else:
                    return 0
            else:
                return dfs(node.left, "left") + dfs(node.right, "right")
        return dfs(root.left, "left") + dfs(root.right, "right")