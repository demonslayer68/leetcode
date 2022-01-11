from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    sum = 0

    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        # reinitializing to be sure
        self.sum = 0

        def recSum(node, num):
            num = num * 2 + node.val
            # if it's a leaf, add to total
            if not node.left and not node.right:
                self.sum += num
            # else call recursively
            else:
                if node.left:
                    recSum(node.left, num)
                if node.right:
                    recSum(node.right, num)

        recSum(root, 0)
        return self.sum
