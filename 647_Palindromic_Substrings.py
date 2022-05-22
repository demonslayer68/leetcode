class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        for i in range(len(s)):
            odd = 1
            even = 1
            left = i - 1
            right = i
            count += 1
            while (odd or even) and left >= 0 and right < len(s):
                if even and s[left] == s[right]:
                    count += 1
                else:
                    even = 0

                if odd and right + 1 < len(s) and s[left] == s[right + 1]:
                    count += 1
                else:
                    odd = 0

                left -= 1
                right += 1

        return count
