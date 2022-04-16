# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        gsum = 0
        def recursive_iterate(node):
            nonlocal gsum
            if node.right:
                recursive_iterate(node.right)
            gsum = node.val = gsum + node.val
            if node.left:
                recursive_iterate(node.left)

        if root:
            recursive_iterate(root)
        return root
