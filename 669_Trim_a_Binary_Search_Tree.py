# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        def trim_low(node, low, parent):
            if node.val < low:
                parent.left = node.right
                if node.right:
                    trim_low(node.right, low, parent)
            elif node.left:
                trim_low(node.left, low, node)

        def trim_high(node, high, parent):
            if node.val > high:
                parent.right = node.left
                if node.left:
                    trim_high(node.left, high, parent)
            elif node.right:
                trim_high(node.right, high, node)

        # first get to a valid root
        while root and (root.val < low or root.val > high):
            if root.val < low:
                root = root.right
            else:
                root = root.left

        if not root:
            return root

        # run above 2 funcs
        if root.left:
            trim_low(root.left, low, root)
        if root.right:
            trim_high(root.right, high, root)

        return root
