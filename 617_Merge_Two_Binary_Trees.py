# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1:
            if root2:
                new_node = TreeNode(root1.val + root2.val)
                new_node.left = self.mergeTrees(root1.left, root2.left)
                new_node.right = self.mergeTrees(root1.right, root2.right)
                return new_node
            else:
                return root1
        elif root2:
            return root2
        else:
            return None
