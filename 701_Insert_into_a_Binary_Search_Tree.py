from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def recursive_insert(node):
            if node.val > val:
                if not node.left:
                    node.left = TreeNode(val)
                else:
                    recursive_insert(node.left)
            else:
                if not node.right:
                    node.right = TreeNode(val)
                else:
                    recursive_insert(node.right)
        if root:
            recursive_insert(root)
        else:
            root = TreeNode(val)
        return root

