# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> list[int]:
        output = []

        def getelements(root, data):
            if root:
                getelements(root.left, data)
                data.append(root.val)
                getelements(root.right, data)

        data1 = []
        data2 = []
        # get all elements individually, then merge. This will be O(n), can't do faster
        getelements(root1, data1)
        getelements(root2, data2)
        i, j = 0, 0
        while i < len(data1) or j < len(data2):
            if i == len(data1) or j < len(data2) and data2[j] < data1[i]:
                output.append(data2[j])
                j += 1
            else:
                output.append(data1[i])
                i += 1
        return output
