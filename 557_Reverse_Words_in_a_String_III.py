class Solution:
    def reverseWords(self, s: str) -> str:
        start = 0
        end = 0
        output = ""
        while end <= len(s):
            if end == len(s) or s[end] == " ":
                for x in range(end - 1, start - 1, -1):
                    output += s[x]
                output += " "
                start = end + 1
            end += 1
        output = output[0:len(s):]
        return output
