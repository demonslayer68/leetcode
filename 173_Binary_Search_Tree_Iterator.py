# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.path = []
        while root:
            self.path.append(root)
            root = root.left

    def next(self) -> int:
        node = self.path.pop()
        rightnode = node.right
        if rightnode:
            self.path.append(rightnode)
            while rightnode.left:
                self.path.append(rightnode.left)
                rightnode = rightnode.left
        return node.val

    def hasNext(self) -> bool:
        return len(self.path)

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
