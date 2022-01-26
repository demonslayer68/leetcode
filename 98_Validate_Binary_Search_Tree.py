from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode], smaller=float("-inf"), larger=float("inf")) -> bool:
        valid = 1
        if root.left:
            valid *= (min(larger, root.val) > root.left.val > smaller and
                       self.isValidBST(root.left, smaller, min(larger, root.val)))
        if root.right:
            valid *= (larger > root.right.val > max(smaller, root.val) and
                      self.isValidBST(root.right, max(smaller, root.val), larger))
        return bool(valid)
