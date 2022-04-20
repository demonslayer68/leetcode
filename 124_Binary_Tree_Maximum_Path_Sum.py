# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.maxpath = float("-inf")

    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        # recursive func which goes through each node and finds the longest possible subtree under it
        # ( tree with one end under it )
        def max_recursive(root):
            if not root:
                return 0

            left_sum = max_recursive(root.left)
            right_sum = max_recursive(root.right)
            # print(root.val, left_sum, right_sum)
            output = root.val
            output += left_sum if left_sum > 0 else 0
            output += right_sum if right_sum > 0 else 0

            # We take the whole path inside this sub-tree and see if that is max
            self.maxpath = max(self.maxpath, output)

            # we take this, because the return value means this is only part of the path. So one end of path is here
            # other end of path is outside. So we need to pick either left or right or neither
            return max(root.val, root.val + left_sum, root.val + right_sum)

        # top return value is useless, since the full path has to be inside tree
        _ = max_recursive(root)

        return self.maxpath
