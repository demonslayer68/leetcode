class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(len(s)//2):
            temp = s[i]
            s[i] = s[-(i+1)]
            s[-(i+1)] = temp

        print(s)

obj = Solution()
obj.reverseString(["h","e","l","l","o"])