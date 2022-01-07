class Solution:
    def partition(self, s: str) -> list[list[str]]:
        palinsets = {}
        palins = set([[i,i] for i in range(len(s))])
        notpalins = set()
        for i in range(1,len(s)):
            if s[i-1] == s[i]:
                palins.add([i-1,i])
            else:
                notpalins.add([i-1,i])
        def ispalin(start, end):
            if [start,end] in palins:
                return True
            elif [start,end] in notpalins:
                return False
            elif start + 1 < end:
                if ispalin(start + 1, end - 1) and s[start] == s[end]:
                    palins.add([start,end])
                    return True
                else:
                    notpalins.add([start,end])
                    return False
            else:
                return False

        # need to further this about how to implement the recursive calls
        def palinsforrange(start):
            if start in palinsets:
                return palinsets[start]
            palinsets[start] = set()
            if start < len(s) - 1:
                palinsets[start] = palinsforrange(start + 1)
                if ispalin(start,end):
                    palinsets[(start,end)] =