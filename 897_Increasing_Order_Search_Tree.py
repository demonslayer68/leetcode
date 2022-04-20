# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        output = self.cur = TreeNode()

        def traverse(node):
            if node:
                traverse(node.left)
                node.left = None
                self.cur.right = node
                self.cur = node
                traverse(node.right)

        traverse(root)
        return output.right