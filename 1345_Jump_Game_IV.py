from collections import defaultdict
from collections import deque

class Solution:
    def minJumps(self, arr: list[int]) -> int:
        steps = [-1] * len(arr)
        visited = set()
        elems = defaultdict(list)
        q = deque()
        nextq = deque()
        q.append(len(arr) - 1)
        jumpcount = 0
        viselems = set()
        for i in range(len(arr)):
            elems[arr[i]].append(i)
        while q:
            index = q.popleft()
            if not index:
                return jumpcount
            visited.add(index)
            if arr[index] not in viselems:
                for x in elems[arr[index]]:
                    if x not in visited:
                        nextq.append(x)
            viselems.add(arr[index])
            if index - 1 >= 0 and arr[index - 1] not in viselems and index - 1 not in visited:
                nextq.append(index - 1)
            if index + 1 < len(arr) and arr[index + 1] not in viselems and index + 1 not in visited:
                nextq.append(index + 1)
            if not q:
                q = nextq
                nextq = deque()
                jumpcount += 1
