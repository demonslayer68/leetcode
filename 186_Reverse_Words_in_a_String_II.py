class Solution:
    def reverse(self, s, start, end):
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1

    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        self.reverse(s, 0, len(s) - 1)
        first = 0
        for last in range(1, len(s) + 1):
            if last == len(s) or s[last] == " ":
                self.reverse(s, first, last - 1)
                first = last + 1

