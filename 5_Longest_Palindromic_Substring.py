class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        pal = []
        longest = 0
        output = [0, 0]
        for i in range(0, length - 1):
            j = [i, i]
            while j[0] > 0 and j[1] < length - 1 and s[j[0] - 1] == s[j[1] + 1]:
                j[0] = j[0] - 1
                j[1] = j[1] + 1
            if j[1] - j[0] + 1 > longest:
                longest = j[1] - j[0] + 1
                output = [j[0], j[1]]
            if s[i] == s[i+1]:
                j = [i, i+1]
                while j[0] > 0 and j[1] < length - 1 and s[j[0] - 1] == s[j[1] + 1]:
                    j[0] = j[0] - 1
                    j[1] = j[1] + 1
                if j[1] - j[0] + 1 > longest:
                    longest = j[1] - j[0] + 1
                    output = [j[0], j[1]]
        return s[output[0]:output[1]+1:1]

obj = Solution()
print( obj.longestPalindrome("cabba") )
