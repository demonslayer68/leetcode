class Solution:
    def __init__(self):
        self.store = {}

    def isMatch(self, s: str, p: str, spos=0, ppos=0) -> bool:
        if spos == 0 and ppos == 0:
            for i in range(0, len(s)+1):
                self.store[str(i)] = {}
        if str(ppos) in self.store[str(spos)]:
            print("using cache for ", spos, ppos)
            return self.store[str(spos)][str(ppos)]

        print("computing", spos, ppos)
        if ppos == len(p):
            if spos == len(s):
                output = True
            else:
                output = False
        elif p[ppos] == "*":
            output = (ppos < len(p) and (self.isMatch(s, p, spos - 1, ppos + 1) or self.isMatch(s, p, spos, ppos + 1))) or (spos < len(s) and (p[ppos - 1] == "." or p[ppos - 1] == s[spos]) and self.isMatch(s, p, spos + 1, ppos))
        elif spos < len(s) and (p[ppos] == "." or p[ppos] == s[spos]):
            output = self.isMatch(s, p, spos + 1, ppos + 1)
        elif ppos < len(p) - 1 and p[ppos + 1] == "*":
            output = self.isMatch(s, p, spos, ppos + 2)
        else:
            output = False

        self.store[str(spos)][str(ppos)] = output
        return output


obj = Solution()
print(obj.isMatch("a", "a*a"))
