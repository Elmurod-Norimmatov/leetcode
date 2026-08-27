# ACCEPTED

from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        queue = deque([root])
        while queue:
            temp = []
            level_size = len(queue)
            for i in range(level_size):
                node = queue.popleft()

                if node.left:
                    queue.append(node.left)
                    temp.append(node.left.val)
                else:
                    temp.append(None)
                
                if node.right:
                    queue.append(node.right)
                    temp.append(node.right.val)
                else:
                    temp.append(None)

            if temp != temp[::-1]:
                return False
        return True