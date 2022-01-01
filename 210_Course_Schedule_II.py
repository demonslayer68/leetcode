class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        visited = [False] * numCourses
        history = [False] * numCourses
        graph = []
        order = []
        for i in range(numCourses):
            graph.append([])
        for j in prerequisites:
            graph[j[1]].append(j[0])

        def dfs(i):
            visited[i] = True
            history[i] = True
            for x in graph[i]:
                if not visited[x]:
                    if not dfs(x):
                        return False
                elif history[x]:
                    return False
            history[i] = False
            order.insert(0,i)
            return True

        for i in range(numCourses):
            if not visited[i]:
                if not dfs(i):
                    return []
        return order

obj = Solution()
print(obj.findOrder(2, [[1, 0]]))