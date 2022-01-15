from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        pairs = (('(', ')'), ('{', '}'), ('[', ']'))
        opening = ('(', '[', '{')
        q = deque()
        for i in range(len(s)):
            if s[i] in opening:
                q.append(s[i])
            elif q and (q[-1], s[i]) in pairs:
                q.pop()
            else:
                return False
        if not q:
            return True
        else:
            return False

