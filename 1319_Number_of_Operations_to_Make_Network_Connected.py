class Node:
    def __init__(self, val=0, nodes=None):
        self.val = val
        self.nodes = nodes if nodes else set()


class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if not n:
            return 0
        self.graphs = -1
        self.redundant = 0
        visited = set()
        nodes = {}
        for i in range(n):
            nodes[i] = Node(i)
        for pair in connections:
            nodes[pair[0]].nodes.add(pair[1])
            nodes[pair[1]].nodes.add(pair[0])

        def dfs(i, parent):
            print(i)
            visited.add(i)
            print(nodes[i].nodes)
            for node in nodes[i].nodes:
                if node not in visited:
                    dfs(node, i)
                else:
                    print(i, node)
                    self.redundant += parent != node
            print("r", self.redundant)

        for i in range(n):
            if i not in visited:
                self.graphs += 1
                dfs(i, -1)
        print(self.graphs)
        return self.graphs if self.graphs <= self.redundant // 2 else -1
