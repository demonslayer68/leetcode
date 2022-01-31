from collections import defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = defaultdict(int)
        for i in range(len(s)):
            count[s[i]] += 1
        for i in range(len(t)):
            count[t[i]] -= 1

        for k, v in count.items():
            if v != 0:
                return False
        return True
