class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        visited = [False] * numCourses
        history = [False] * numCourses
        graph = []
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
            return True

        for i in range(numCourses):
            if not visited[i]:
                if not dfs(i):
                    return False
        return True

obj = Solution()
print(obj.canFinish(2, [[1, 0],[0, 1]]))