# Marking this as challenging mainly for the tree type binary tree search algo


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0
        temp = root
        levels = 0
        while temp != None:
            temp = temp.left
            levels += 1

        # total number of nodes till n-1 level
        nodes = 2 ** (levels - 1) - 1

        # number of levels in rightmost nodes of left node of this node. This gives the middle leaf node under this node
        def remaining_levels(node):
            if not node.left:
                return 1

            # min 2 since left exists
            temp_levels = 2
            left_node = node.left
            while left_node.right:
                left_node = left_node.right
                temp_levels += 1
            return temp_levels

        temp = root
        while levels > 0 and temp:
            # check if middle node exists
            mid_level = remaining_levels(temp)
            # print(levels, nodes)
            # if it does, add all left side leaf nodes to count, move to right side.
            # else no addition, move to left side
            if mid_level == levels:
                if levels == 1:
                    nodes += 1
                else:
                    nodes += 2 ** (levels - 2)
                temp = temp.right
            else:
                temp = temp.left
            # subtract level, since we moved one level lower
            levels -= 1
        return nodes