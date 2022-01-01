class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        tree = []
        incount = [0] * numCourses
        order = []
        top = set(range(numCourses))
        for i in top:
            tree.append([])
        for j in prerequisites:
            tree[j[1]].append(j[0])
            incount[j[0]] = incount[j[0]] + 1
            top.discard(j[0])

        while top:
            root = top.pop()
            order.append(root)
            for x in tree[root]:
                incount[x] = incount[x] - 1
                if not incount[x]:
                    top.add(x)

        if len(order) == numCourses:
            return True
        else:
            return False

obj = Solution()
print( obj.canFinish(2, [[1,0]]) )