class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        curr = []
        maxlen = 0
        for i in range(0, len(s)):
            if s[i] in curr:
                index = curr.index(s[i])
                clen = len(curr)
                if (clen > maxlen):
                    maxlen = clen
                curr = curr[index + 1:clen:1]
            curr.append(s[i])
            clen = len(curr)
            if (clen > maxlen):
                maxlen = clen
        return maxlen

obj = Solution()
print(obj.lengthOfLongestSubstring("aab"))