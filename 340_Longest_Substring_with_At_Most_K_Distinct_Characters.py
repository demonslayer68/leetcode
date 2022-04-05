class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if k == 0:
            return 0
        chars = {}
        start = 0
        output = 0
        for index in range(len(s)):
            elem = s[index]
            if len(chars) == k and elem not in chars:
                remove = min(chars, key=chars.get)
                start = chars[remove] + 1
                del (chars[remove])
            chars[elem] = index
            output = max(output, index - start + 1)
        return output
