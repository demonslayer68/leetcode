
# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        visited = {}

        def rec_clone(oldnode):
            newn = []
            newnode = Node(oldnode.val, newn)
            visited[oldnode.val] = newnode
            for neighbor in oldnode.neighbors:
                if neighbor.val in visited:
                    newn.append(visited[neighbor.val])
                else:
                    newn.append(rec_clone(neighbor))
            newnode.neighbors = newn
            return newnode

        if not node:
            return node
        else:
            return rec_clone(node)


