class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        chars = {}

        if len(s2) < len(s1):
            return False

        #create table of chars
        for i in range(len(s1)):
            if s1[i] in chars:
                chars[s1[i]] += 1
            else:
                chars[s1[i]] = 1

        #capture freq of first n chars
        for j in range(len(s1)):
            if s2[j] in chars:
                chars[s2[j]] -= 1
            else:
                chars[s2[j]] = -1

        #move n window, each time checking if all chars are found( count of each = 0 )
        for j in range(len(s1), len(s2)):
            if not any(chars.values()):
                return True
            if s2[j] in chars:
                chars[s2[j]] -= 1
            else:
                chars[s2[j]] = -1
            if s2[j - len(s1)] in chars:
                chars[s2[j - len(s1)]] += 1
            else:
                chars[s2[j - len(s1)]] = 1
        if not any(chars.values()):
            return True
        return False


obj = Solution()
print(obj.checkInclusion("adc", "dcda"))
