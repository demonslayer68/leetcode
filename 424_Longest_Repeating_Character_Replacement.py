from collections import defaultdict
from collections import deque


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        q = defaultdict(deque)
        maxl = 0
        for i in range(len(s)):
            q[s[i]].append(i)
            while i - q[s[i]][0] + 1 > k + len(q[s[i]]):
                q[s[i]].popleft()
            maxl = max(maxl, k + len(q[s[i]]))
        return min(maxl, len(s))
