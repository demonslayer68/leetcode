class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        pal = []
        longest = 1
        output = [0, 0]
        for i in range(0, length - 1):
            pal.append([i, i])
            if s[i] == s[i+1]:
                pal.append([i, i+1])
                longest = 2
                output = [i, i + 1]
        newpal = pal
        while newpal:
            pal = newpal.copy()
            newpal = []
            for j in pal:
                if j[0] > 0 and j[1] < length - 1 and s[ j[0] - 1 ] == s[j[1] + 1]:
                    newpal.append([j[0] - 1, j[1] + 1])
                    if j[1] - j[0] + 3 > longest:
                        longest = j[1] - j[0] + 3
                        output = [j[0] - 1, j[1] + 1]
        return s[output[0]:output[1]+1:1]

obj = Solution()
print( obj.longestPalindrome("cabba") )
