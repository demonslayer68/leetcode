from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> list[int]:
        output = []
        mem = {}
        if not root:
            return output
        maxlevel = 0

        def traverse(node, level):
            nonlocal maxlevel
            if node.left:
                traverse(node.left, level + 1)
            mem[level] = node.val
            if node.right:
                traverse(node.right, level + 1)
            maxlevel = max(maxlevel, level)

        traverse(root, 0)
        for i in range(maxlevel + 1):
            output.append(mem[i])
        return output
