import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub("[\W_]", "", s)
        s = s.lower()
        for i in range(int(len(s)/2)):
            if s[i] != s[len(s)-i-1]:
                return False

        return True


obj = Solution()
print(obj.isPalindrome("A man, a plan, a canal: Panama"))

