from collections import Counter
from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t:
            return ""
        cnt = Counter(t)
        output = ""
        right = 0
        left = 0
        while right < len(s):
            if s[right] in cnt:
                # if you find a present char, subtract its count
                cnt[s[right]] -= 1
                # if all counts are less than 0, then keep moving left, till count comes back > 0
                if cnt[s[right]] <= 0 and max(cnt.values()) <= 0:
                    while left <= right:
                        #print(left, right)
                        if s[left] in cnt:
                            cnt[s[left]] += 1
                            # this means, if we remove left, then remaining string does not contain all chars
                            # ie, this combination of left and right is the min substring with all chars
                            # so take the length of this and see if its smallest. Then go back to moving right again
                            if cnt[s[left]] > 0:
                                if output == "" or len(output) > right - left + 1:
                                    output = s[left:right+1]
                                    #print(output)
                                left += 1
                                break
                        left += 1
            right += 1
        return output