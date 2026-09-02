from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
       if not root:
           return
       
       res = []
       queue = deque([root])
       while queue:
           level_size = len(queue)
           s = 0
           for i in range(level_size):
               node = queue.popleft()
               s += node.val
               
               if node.left:
                   queue.append(node.left)
               
               if node.right:
                   queue.append(node.right)
           res.append(s/level_size)
       return res