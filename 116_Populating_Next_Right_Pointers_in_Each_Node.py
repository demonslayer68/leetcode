from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next



class Solution:
    next_by_level = {}

    def connect(self, root: 'Optional[Node]', level=0) -> 'Optional[Node]':
        if not level:
            self.next_by_level = {}
        if root:
            if level in self.next_by_level:
                root.next = self.next_by_level[level]
            self.next_by_level[level] = root
            root.right = self.connect(root.right, level + 1)
            root.left = self.connect(root.left, level + 1)
        return root
