class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        left = 0
        right = 0
        chars = {}
        output = 0
        while right < len(s):
            if s[right] not in chars:
                chars[s[right]] = 1
                if len(chars) == 3:
                    output = max(output, right - left)
                    while left < right:
                        chars[s[left]] -= 1
                        if not chars[s[left]]:
                            del(chars[s[left]])
                            left += 1
                            break
                        left += 1
            else:
                chars[s[right]] += 1
            right += 1
        output = max(output,right - left)
        return output
    