from collections import defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        indset = set()
        track = defaultdict(list)
        count = defaultdict(int)
        tsize = len(t)
        start = len(s)
        minstring = ""
        for elem in t:
            count[elem] += 1
        for i in range(len(s)):
            if count[s[i]] > 0:
                start = min(i, start)
                count[s[i]] -= 1
                tsize -= 1
                track[s[i]].append(i)
                indset.add(i)
            elif track[s[i]]:
                elem = track[s[i]].pop(0)
                indset.remove(elem)
                indset.add(i)
                track[s[i]].append(i)
                if start == elem:
                    start = min(indset)
            if not tsize:
                if not minstring or len(minstring) > i - start + 1:
                    minstring = s[start:i + 1:1]
        return minstring
